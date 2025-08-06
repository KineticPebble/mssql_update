import time

import paramiko.ecdsakey
start_time = time.time()
import pandas as pd
import sql_con
import datetime as dt
import procedure
import sftpop
import datetime as dt
import variable
import glob, os
import pysftp
from base64 import decodebytes
import paramiko
import pandas as pd
import re

datafile_JBP = 'JBP_'
datafile_JWAT = 'JWAT_'
datafile_NLUU = 'NUU_'
datafile_RJ =  'RJR_'

host = '10.10.10.10'
keydata = b"""ECDSAKey here"""
key = paramiko.ECDSAKey(data=decodebytes(keydata))
cnopts = pysftp.CnOpts()
cnopts.hostkeys.add(host, 'ssh-rsa', key)

sftp = sftpop.Sftp(hostname=host, username='username', password='password', port=1234, cnopts=cnopts)
sftp.connect()

download_loc = 'D:/Files/Input/JBP'
source_loc = './'
source_loc_H = 'Historical Reports/'
recipt_loc = '../KPB/'

yt = variable.ytdmy_
ymd = yt = variable.tdymd

folders = ['ABC', 'DEF', 'GHI', 'JKL', 'Receipt']

for path in list(folders):
    old_file = glob.glob(download_loc+"/"+path+"/*")
    for c in old_file:
        os.remove(c)

def get_latest(datafile, source_loc, pattern):
    print(source_loc)
    filelist = []
    print(datafile)
    if source_loc == recipt_loc:
        ls = sftp.listdir(source_loc)
        for i in ls:
            if re.match(pattern, i):
                filelist.append(i)
    else:
        for folder in folders[:-1]:
            ls = sftp.listdir(source_loc+folder)
            for i in ls:
                if re.match(pattern, i):
                    filelist.append(folder+'/'+i)
    print(filelist)
    return filelist

def download_file(datafile, historical=False):
    download_loc = 'D:/Files/Input/JBP'
    source_loc = './'
    yt = variable.ytdmy_
    if historical == True:
        source_loc = source_loc_H
        pattern = '^'+datafile
    elif historical == 'Receipt':
        source_loc = recipt_loc
        pattern = '^'+datafile+ymd
    else: pattern = '^'+datafile+'.+'+yt
    target_file = get_latest(datafile, source_loc, pattern)
    for filename in list(target_file):
        if historical == 'Receipt': sftp.download(source_loc+filename, download_loc+"/"+'Receipt'+"/"+filename)
        else: sftp.download(source_loc+filename, download_loc+"/"+filename)
    if historical == 'Receipt':
        target_file = ['Receipt'+"/"+i for i in list(target_file)]
    return target_file

database = "COFP"
connection = sql_con.get_con(database)

def read_files(target_file, historical=False):
    count = 0
    dfs = []
    for filename in list(target_file):
        try:
            if historical == 'Receipt':
                df = pd.read_csv(download_loc+"/"+filename, dtype=str, usecols=[i for i in range(58)])
            else:
                df = pd.read_csv(download_loc+"/"+filename, parse_dates=['Date'], date_format="%d-%m-%Y")
                df['Filename'] = filename.split('/')[-1]
                if "NUU_" in filename:
                    df.rename(columns={"Mobile No": "Sender ID"}, inplace=True)
        except pd.errors.EmptyDataError:
            count += 1
        dfs.append(df)
    df = pd.concat(dfs, ignore_index=True,)
    print(count)
    return df
    
# df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')

JBP = ''' INSERT INTO [COFP].dbo.JBP

      values(?,?,?,?,?,?,?)
'''

JAT = ''' INSERT INTO [COFP].dbo.JWAT

      values(?,?,?,?,?,?)

      '''
LUU = ''' INSERT INTO [COFP].dbo.LUU

      values(?,?,?,?,?,?,?)

      '''

RJ = ''' INSERT INTO [COFP].dbo.[Receipt]

      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

      '''

jbp = "JBP"
jat = "JWAT"
luu = "LUU"
rj = "[Receipt]"

def truncate(table, cursor):
    sqldq = f"delete from [COFP].dbo.{table}"
    cursor.execute(sqldq)
    cursor.commit()

def update(df, query, cursor):
    all_df = df.fillna('')
    cursor.fast_executemany = True
    df_list = all_df.values.tolist()
    df_list = procedure.fill_null(df_list)
    for i in range(0, len(df_list), 25000):
        cursor.executemany(query, df_list[i:i + 25000])
        print(i)
        cursor.commit()
    print(len(df_list))
    cursor.close()


def main(datafile, table, query, cursor, historical=False):
    target_file = download_file(datafile, historical=historical)
    if historical == True or historical == 'Receipt':
        df = read_files(target_file, historical='Receipt')
        truncate(table, cursor)
    else: df = read_files(target_file)
    update(df, query, cursor)



# main(datafile_JBP, jbp, JBP, cursor=connection.cursor(), historical=True)
# main(datafile_JWAT, jat, JAT, cursor=connection.cursor(), historical=True)
# main(datafile_NLUU, luu, LUU, cursor=connection.cursor(), historical=True)

main(datafile_JBP, jbp, JBP, cursor=connection.cursor())
main(datafile_JWAT, jat, JAT, cursor=connection.cursor())
main(datafile_NLUU, luu, LUU, cursor=connection.cursor())

# main(datafile_RJ, rj, RJ, cursor=connection.cursor(), historical='Receipt')

sftp.disconnect()

