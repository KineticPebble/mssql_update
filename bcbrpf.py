import time
start_time = time.time()
import pandas as pd
import sql_con
import datetime as dt
import procedure
from sftpop import sftp
import datetime as dt
import variable
import glob, os


sftp.connect()
download_loc = 'D:/Files/Input/bcbr_pf'
source_loc = 'main/PF'
td = variable.tdmdy
SP = 'exec [PROD].dbo.PF_SP'

old_file = glob.glob(download_loc+"/*")
for c in old_file:
    os.remove(c)

def get_latest():
    ls = sftp.listdir(source_loc)
    for i in ls:
        if f"PFDump_{td}.csv" in i:
            return i
    print("File not found")
    sftp.disconnect()
    exit()

target_file = get_latest()
sftp.download(source_loc+"/"+target_file, download_loc+"/"+target_file)
sftp.disconnect()

database = "PROD"
connection = sql_con.get_con(database)

dates = ['OLSC_Time', 'Order_Date', 'First_Assigned_Date', 'Shipped_Date']

df = pd.read_csv(download_loc+"/"+target_file, dtype=str)

for i in list(dates):
    df[i] = pd.TimedeltaIndex(pd.to_numeric(df[i]), unit='D') + dt.datetime(1899, 12, 30)
    df[i] = df[i].dt.strftime('%d-%m-%Y')

bcbr = ''' INSERT INTO [PROD].[dbo].[PF_Temp]

      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

sqldq = f"delete from [PROD].[dbo].[PF_Temp]"
cursor = connection.cursor()
cursor.execute(sqldq)
cursor.commit()

all_df = df.fillna('')
cursor.fast_executemany = True
df_list = all_df.values.tolist()
df_list = procedure.fill_null(df_list)
for i in range(0, len(df_list), 25000):
    cursor.executemany(bcbr, df_list[i:i + 25000])
    print(i)
    cursor.commit()
print(len(df_list))
cursor.close()

print("running SP")
os.system(f'''cmd /c sqlcmd -Q " {SP} " -o "D:\SAP_files\Logs\Validation\pick_fail.csv" -s "," ''')
print("--- %s seconds ---" % (time.time() - start_time))