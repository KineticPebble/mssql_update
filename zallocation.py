import time
start_time = time.time()
import auth
import pandas as pd
import sql_con
import procedure
from ftplib import FTP
import variable
import glob, os
import re
import teams_msg

download_loc = 'D:/Files/ZAllocation/Files To Upload'
source_loc = 'ZALLOCATION_OUTPUT'

ftp = FTP(host=auth.ftp_host)
ftp.login(user=auth.ftp_usr, passwd=auth.ftp_passwd)
ftp.cwd(source_loc)
zaf = ftp.nlst()
r = re.compile(f"^BD\d+_F2_\d+_{variable.tddmynu}\.xls$")
files = list(filter(r.match, zaf))

for filename in files:
    with open(download_loc+"/"+filename, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)

SP = 'exec [INVT].[dbo].[ZAllocation_SSIS_Insert] '
database = "INVT"
connection = sql_con.get_con(database)

num = ['Current Stock', 'Pending MIRO Qty',	'Open STO Qty',	'Open SO Qty',	'Blocked Stock',	'Open Del Qty', 'Qty Avail. for Alloc.', 'MRP']

filenames = [x for x in os.listdir(download_loc) if '.xls' in x]
dfs = []
for f in filenames:
    print(download_loc+"/"+f)
    df = pd.read_csv(download_loc+"/"+f, dtype=str, encoding='ansi', delimiter="\t")
    for i in list(num):
        df[i] = pd.to_numeric(df[i])
    dfs.append(df)

try:
    df = pd.concat(dfs, ignore_index=True)
except:
    teams_msg.msg_teams("file not found", 'Zallocation error')
    exit()


df.drop(['Brand Name'], axis=1, inplace=True)

zallocation = ''' INSERT INTO [INVT].[dbo].[ZAllocation_SSIS]

      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

sqldq = f"truncate table [INVT].dbo.ZAllocation_SSIS"
cursor = connection.cursor()
cursor.execute(sqldq)
cursor.commit()

all_df = df.fillna('')
cursor.fast_executemany = True
df_list = all_df.values.tolist()
df_list = procedure.fill_null(df_list)
for i in range(0, len(df_list), 25000):
    cursor.executemany(zallocation, df_list[i:i + 25000])
    print(i)
    cursor.commit()
print(len(df_list))
cursor.close()

print("running SP")
os.system(f'''cmd /c sqlcmd -Q " {SP} "  -o "D:\SAP_files\Logs\Validation\zallocatio.csv" -s "," ''')
print("--- %s seconds ---" % (time.time() - start_time))
teams_msg.msg_teams("Zallocation Complete", 'Zallocation Complete')