''' Script to update all the Key Partners sales and stock file to their tespective tables in SQL

3 functions:
    - HR_Filter
    - convert_to_csv
    - loading

first the kp_variable_new script checks all the files and gives all the fullpath of the partner files.
loading is the main function which incorporates all other function.
Different files have different tables and require different things.
'''

import time
start_time = time.time()
import win32com.client
import pandas as pd
import sql_con
import kp_variable_new
from datetime import date
import os
import variable

database = "SDPD"
connection = sql_con.get_con(database)

def HR_filter(df: pd.DataFrame) -> pd.DataFrame:
    '''Filter Shopppers Haryana stock file

    Parameters:
        df: Pandas Dataframe

    Returns:
        Filtered Dataframe
    '''
    df = df[df["Brand"].isin(["JJ&J", "JJ", "ON", "VM"])]
    return df

def covert_to_csv(filenm: list, csv_location: str) -> list:
    '''Convert Excel files to CSV file using excel application

    Parameters:
        filenm: List of files
        csv_location: Location where csv will be saved

    Returns: 
        list of creted csv file locations
    '''
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Application.DisplayAlerts = False 
    newname_list = []
    for n in filenm:
        doc = excel.Workbooks.Open(n)
        v = doc.Sheets.Count
        for i in range(v):
            newname = csv_location+"\\"+n.split("\\")[-1]+str(i+1)+".csv"
            doc.Sheets(i+1).Select()
            newname_list.append(newname)
            print(newname)
            doc.SaveAs(newname, 6)
        doc.Close(SaveChanges=False)
    excel.Application.Quit()
    return newname_list

timestamp = pd.to_datetime('now').replace(microsecond=0)

def loading(filename: list, partner: str, table: str, cursor: object, sqlqi: str, dtype: dict | str =None, header: int =0, parse_date: list =None, dayfirst: bool =False, encoding: str ='ansi') -> None:
    '''This is the main function which load each file in datafram, modifies according to it's table structure and loads it in table

    Parameters:
        filename: List of filename
        partner: Partner and and datatype
        table: table name where the data will be uploaded
        cursor: SQL connection cursor object.
        sqlqi: The query used to update the table
        dtype: Datatype used in dataframe
        header: Header row in the file
        parse_date: Date column to parse date
        dayfirst: For taking day as first value from Date
        encoding: encoding used in the Dataframe

    Returns:
        None
    '''
    print(partner)
    ftd = []
    for ft in list(filename):
        filedate = os.path.getctime(ft)
        t_obj = time.ctime(filedate)
        m_ti = time.strptime(t_obj)
        datefile = time.strftime("%Y-%m-%d", m_ti)
        ftd.append(datefile)
    if "Lifestyle" not in filename[0]:
        fname_list = covert_to_csv(filename, kp_variable_new.csv_location)
    else: fname_list = filename
    dfs = []
    for f, t in zip(fname_list, ftd):
        # if "Stock_KPBS" in f:
        #     df = pd.read_csv(f, index_col=None, dtype=dtype, header=4, parse_dates=parse_date, dayfirst=dayfirst, encoding=encoding)
        # else:
        #     # print(f)
        if "KPBS" in f: df = pd.read_csv(f, index_col=None, dtype=dtype, header=2, parse_dates=parse_date, dayfirst=dayfirst, encoding=encoding)
        else: df = pd.read_csv(f, index_col=None, dtype=dtype, header=header, parse_dates=parse_date, dayfirst=dayfirst, encoding=encoding)
        if "Sales" in partner:
            if "Kapsons" in partner or "Shoppers" in partner:
                df.drop(df.tail(1).index,inplace=True)
            if "Kapsons" in partner:
                if "KPBS" in f:
                    df['LOT NO'] = df['LOT NO'].str.replace("/\d+", '', regex=True)
                    df.insert(len(df.columns), 'OTHER DEDUCTIONS', '0')
                    df.insert(len(df.columns), 'DISC RS', '0')
                    df.insert(len(df.columns), 'OTHER BONUS DISCOUNT', '0')
                    df.insert(len(df.columns), 'GIFT COUPON AMOUNT', '0')
                    df.insert(len(df.columns), 'SCHEME NAME', '')
                    df.insert(len(df.columns), 'TAX 3', '0')
                    df.insert(len(df.columns), 'TOTAL TAX', '0')
                    df.insert(len(df.columns), 'SPECIAL SCHEME NAME', '')
                    df.insert(len(df.columns), 'BASIC RATE', '0')
                    df.insert(len(df.columns), 'GIFT VOUCHER AMOUNT', '0')
                    df = df[kp_variable_new.kp_bs_sales_columns]
                else:
                    df = df.drop(['GIFT COUPON NAME', 'MOBILE SCHEME MOBILE NUMBER'], axis=1)
                a = list(df['LOT NO'][~df['LOT NO'].str.isdigit()].index)
                for b in a:
                    df.at[b, 'LOT NO'] = '0'
            if "Shoppers" in partner:
                df = df.drop(['Distribution\nChannel', 'Store No.'], axis=1)
            print(list(df.columns))
            df['FileNm'] = f.split("\\")[-1]
            df['Load_TimeStamp'] = timestamp
        elif "Stock" in partner:
            if "Blue" in partner:
                df.insert(5, "Desc4", '')
                df['FileName'] = f.split("\\")[-1]
                df['Date'] = t
                df['UploadTimestamp'] = pd.to_datetime('now').replace(microsecond=0)  
            else:
                if "Kapsons" in partner or "Shoppers" in partner:
                    if "KPBS" in f:
                        df.insert(len(df.columns), 'LOOK NAME', '')
                        df.insert(len(df.columns), 'ITEM DESC OUR', '')
                        df.insert(len(df.columns), 'STYLE NAME', '')
                        df.insert(len(df.columns), 'PUR RATE', 0)
                        df.insert(len(df.columns), 'PURCHASE RETURN VALUE', 0)
                        df.insert(len(df.columns), 'BASIC RATE', 0)
                        df.insert(len(df.columns), 'SALE RATE', 0)
                        df.insert(len(df.columns), 'PURCHASE VALUE', 0)
                        # print(df.columns)
                        df = df[kp_variable_new.kp_bs_stock_columns]
                    else:
                        df.drop(df.tail(1).index,inplace=True)
                if "Shoppers" in partner:
                    df.drop(['Store No.'], axis=1, inplace=True)
                    if "Stock_SS_HR" in f:
                        df = HR_filter(df)
                df['UploadTimestamp'] = pd.to_datetime('now').replace(microsecond=0)
                df['Date'] = t
                df['FileName'] = f.split("\\")[-1]
        dfs.append(df)
    sqlq = f"delete from {table} "
    cursor.execute(sqlq)
    cursor.commit()
    all_df = pd.concat(dfs, ignore_index=True)
    all_df = all_df.fillna('')
    cursor.fast_executemany = True
    df_list = all_df.values.tolist()
    for i in range(0, len(df_list), 25000):
        cursor.executemany(sqlqi, df_list[i:i + 25000])
        print(i)
        cursor.commit()
    print(len(df_list))
    cursor.close()


loading(kp_variable_new.Kapsons_sales, "Kapsons_Sales", "SDPD.dbo.SIS_K", connection.cursor(),
        kp_variable_new.Kapsons_sales_sqlq, str, 3, encoding='ansi')

loading(kp_variable_new.Kapsons_stock, "Kapsons_Stock", "[INVT].[dbo].[KS] ", connection.cursor(),
        kp_variable_new.Kapsons_stock_sqlq, str, 4)

loading(kp_variable_new.Blue_club_sales, "Blue Club_Sales", "[SDPD].[dbo].[SIS_BC]", connection.cursor(),
        kp_variable_new.blue_club_sales_sql, kp_variable_new.BC_sales_datatype, 0, parse_date=['DATE'], dayfirst=True)

loading(kp_variable_new.Lifestyle_sales, "Lifestyle_Sales", "[SDPD].[dbo].[SIS_LS]", connection.cursor(),
        kp_variable_new.Lifestyle_sales_sqlq, str, 0)

loading(kp_variable_new.Lifestyle_stock, "Lifestyle_Stock", "[INVT].[dbo].[LS_S]", connection.cursor(),
        kp_variable_new.Lifestyle_stock_sqlq, str, 0)

loading(kp_variable_new.Shoppers_sales, "Shoppers_Sales", "[SDPD].[dbo].[SIS_S]", connection.cursor(),
        kp_variable_new.shoppers_sales_sqlq, str, 4)

loading(kp_variable_new.all_shopeprs_stock, "Shoppers_Stock", "[INVT].[dbo].[SS_S]", connection.cursor(),
       kp_variable_new.shoppers_stock_sqlq, str, 3)



connection.close()

os.system(f'''cmd /c sqlcmd -Q " EXEC [SDPD].[dbo].[DRS] @date = '{variable.ytymd}' ,@Upload_Month = N'Dec-23' " -o "D:\SAP_files\Logs\Validation\KP_Sales.csv" -s "," ''')

os.system('''cmd /c sqlcmd -i "D:\Scripts\mssql_update\Stock_date_updated.sql" ''')

os.system(f'''cmd /c sqlcmd -Q " EXEC [INVT].[dbo].[DRSS] @date = '{variable.tdymd}' "  -o "D:\SAP_files\Logs\Validation\KP_Stock.csv" -s "," ''')


