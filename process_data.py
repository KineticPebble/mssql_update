'''This file conaines all the function required for processing files

3 functions:
    - convert_csv
    - get_data
    - sql_insert
'''

import win32com.client
import variable
import pandas as pd
import os

def covert_to_csv(filenm: list) -> list:
    '''converts excel file to csv

    Parameters:
        filenm: List containing filenames

    Returns:
        csv filenames
    '''
    excel = win32com.client.Dispatch("Excel.Application")
    ls = {i:excel.Workbooks.Open(variable.location+"\\"+i) for i in filenm}
    newname_list = []
    for i, doc in ls.items():
        newname = variable.location+'\\'+i.replace("XLSX", "csv")
        newname_list.append(newname)
        #print(newname)
        if os.path.exists(newname):
            continue
        doc.SaveAs(newname, 6)
        doc.Close(SaveChanges=False)
    excel.Application.DisplayAlerts = False 
    excel.Application.Quit()
    return newname_list

def get_data(filenm: list) -> pd.DataFrame:
    '''use the conver_to_csv function and pandas to craete dataframe and modify data according to requirements
    
    Parameters:
        filenm: List containing filenames

    Returns:
        all_df: modified pandas dataframe
    '''
    if filenm != variable.dc_stock:
        newname_list = covert_to_csv(filenm)
    else: newname_list =  [variable.location+'\\'+x for x in filenm]
    dfs = []
    for name in newname_list:
        if filenm == variable.zsis:
            df = pd.read_csv(name, dtype=str, encoding="ansi", skiprows=[1])
        elif filenm == variable.dc_stock:
            df = pd.read_csv(name, dtype=str, encoding="ansi", delimiter="|", header=4)
            df.drop(df.head(1).index,inplace=True)
            df.drop(df.tail(3).index,inplace=True)
            df.columns = variable.dc_stock_columns
        else:
            df = pd.read_csv(name, dtype=str, encoding="ansi")
        dfs.append(df)
        print(name, len(df))
    if filenm == variable.tender_files:
        for i in range(len(dfs)):
            dfs[i].drop(dfs[i].tail(1).index,inplace=True)
    all_df = pd.concat(dfs, ignore_index=True)
    all_df = all_df.fillna('')
    # all_df = all_df.where(pd.notnull(df), None)
    # all_df = all_df.values.tolist()
    return all_df

def sql_insert(data: list, sqlq: str, cursor: object) -> None:
    '''function for inserting data into sql table

    Parameters:
        data: 2 Dimentional list contaning tabular data
        sqlq: SQL insert qurey text
        cursor: Database cursor object
    
    Returns:
        None
    '''
    cursor.fast_executemany = True
    for i in range(0, len(data), 25000):
        cursor.executemany(sqlq, data[i:i + 25000])
        print(i)
    cursor.commit()
    cursor.close()
    print(len(data))
