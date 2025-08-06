import time
start_time = time.time()
import pandas as pd
from sql_con import get_con
import procedure
# import logging
import process_data
import win32com.client

fname = r"D:\Files\Input\Online DSR\Online DSR.xlsb"
def convert_to_csv(fname):
    excel = win32com.client.Dispatch("Excel.Application")
    doc = excel.Workbooks.Open(fname)
    newname = fname.replace("xlsb", 'csv')
    excel.Application.DisplayAlerts = False 
    doc.Sheets("Sheet1").Select()
    doc.SaveAs(newname, 6)
    doc.Close(SaveChanges=False)
    excel.Application.Quit()
    newname = newname.replace('\\', '/')
    return newname

def load_df(newname):
    df = pd.read_csv(newname, encoding='ansi', parse_dates=['New Date'], dayfirst=True, dtype=str)
    df['Net Unit'] = df['Net Unit'].fillna('1')
    df['Net Value'] = df['Net Value'].fillna('1')
    df['Net Unit'] = df['Net Unit'].str.replace('^0$', '1', regex=True)
    df['Net Value'] = df['Net Value'].str.replace('^0$', '1', regex=True)
    df['GMV'] = df['GMV'].fillna('1')
    df['Unit Sold'] = df['Unit Sold'].fillna('1')
    df['Final GMV'] = df['Final GMV'].fillna('1')
    df['GMV'] = df['GMV'].str.replace('^0$', '1')
    df['Unit Sold'] = df['Unit Sold'].str.replace('^0$', '1', regex=True)
    df['Final GMV'] = df['Final GMV'].str.replace('^0$', '1', regex=True)


    return df

sqlq = '''
INSERT INTO [SSF].[dbo].[Online_DSR_Bot]

      Values(?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?)
'''

def load(df, conx):
    cursor=conx.cursor()
    cursor.execute(" delete from [SSF].[dbo].[Online_DSR_Bot] ")
    cursor.commit()
    cursor.close()
    df = df.fillna('')
    df = df.values.tolist()
    df = procedure.fill_null(df)
    process_data.sql_insert(df, sqlq, cursor=conx.cursor())

conx = get_con('SSF')
newname = convert_to_csv(fname)
df = load_df(newname)
load(df, conx)

cursor=conx.cursor()
cursor.execute(" exec SSF.dbo.Online_DSR_Bot_SP ")
cursor.commit()
cursor.close()


print("--- %s seconds ---" % (time.time() - start_time))

    
