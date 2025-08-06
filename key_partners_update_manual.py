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
from datetime import date
import os, glob

csv_location=r"C:\Users\USER\Downloads\csv"

kp_location = r"C:\Users\USER\Downloads"

shoppers_stock_path = kp_location+'\\'+'Shoppers'

csv_list = glob.glob(csv_location+r'\*')
for c in csv_list:
    os.remove(c)

database = "SDPD"
connection = sql_con.get_con(database)

Blue_club_sales = [kp_location+"\\"+i for i in ['Sales_BC_March.xlsx']]

Kapsons_sales = [kp_location+"\\"+i for i in ['SaleReport(1).xls',
'SaleReport(2).xls',
'SaleReport(3).xls',
'SaleReport(4).xls',
'SaleReport.xls',
]]
Kapsons_stock = [kp_location+"\\"+i for i in ['StockReport.xls']+[f'StockReport({i}).xls' for i in range(1,15)]]

Lifestyle_sales = [kp_location+"\\"+i for i in ['Sales_Itemwise_Date_Report_1260.csv']]
Lifestyle_stock = [kp_location+"\\"+i for i in ['Stock_Details_Itemwise_Report_1260.csv', 'Stock_Details_Itemwise_Report_44627.csv']]

Shoppers_sales = [kp_location+"\\"+i for i in ['SalesDetails.xlsx', 'SalesDetails(1).xlsx']]
# Shoppers_stock = ['StockDetails.xlsx']+[f'StockDetails({i}).xlsx' for i in range(1, 76)]
Shoppers_stock = os.listdir(shoppers_stock_path)
Shoppers_stock = [shoppers_stock_path+"\\"+i for i in Shoppers_stock]
                  
JB_sales = ["J&J Sales.xlsx", "SL Sales.xlsx"]

JB_stock = ["J&J Stock Report.xlsx", "Selected Stock Report.xlsx"]

BC_sales_datatype = {'BRAND': str, 'SITE NAME': str, 'DIVISION': str, 'CAT2': str, 'BILL NO': str, 'SECTION': str,
       'PRODUCT': str, 'CODE': str, 'ITEMDESC6': str, 'COLOR': str, 'SIZE': str, 'SALE QTY': float,
       'MRPAMT(A)': float, 'PRMOAMT(B)': float, 'ITEMDISCOUNTAMT(C)': float, 'BILLDISCOUNTAMT(D)': float,
       'LPDISCOUNTAMT(E)': float, 'EXTAXAMT FACTOR(F)': float, 'Net Amt': float}

BC_stock_datatype = {"Sitename": str, "Section": str, "Category2": str, "Brand": str, "Department": str, "Division": str,
"Color": str, "Stylecode": str, "Desc6": str, "Size": str, "Fit": str, "Quantity": float, "MRP": float
}

kp_bs_sales_columns = ['S. NO.',	'COMPANY NAME',	'BILL DATE',	'BILL NO',	'BRAND NAME',	'ITEM GROUP NAME',	'ITEM SUB GROUP NAME',	'ITEM NAME',	
                       'LOT NO',	'USER ITEM CODE',	'LOT CODE',	'COLOR NAME',	'SIZE',	'MRP RATE',	'SALE QUANTITY',	'SALE VALUE',	
                       'SALE RETURN QUANTITY',	'SALE RETURN VALUE',	'NET SALE QUANTITY',	'NET SALE VALUE',	'NET SALE AFTER ADJ',	
                       'SEASON NAME',	'DISCOUNT',	'SPECIAL DISCOUNT',	'OTHER DEDUCTIONS',	'DISC RS',	'OTHER DISCOUNT',	'OTHER BONUS DISCOUNT',	
                       'GIFT COUPON AMOUNT',	'TOTAL DISCOUNT',	'SCHEME NAME',	'TAX TYPE',	'REMARKS1',	'TAX 3',	'TOTAL TAX',	'REMARKS2',	
                       'HSN CODE',	'SPECIAL SCHEME NAME',	'SALE RATE',	'BASIC RATE',	'GIFT VOUCHER AMOUNT'
]
kp_bs_stock_columns = ['S. NO.',	'COMPANY NAME',	'SEASON NAME',	'BRAND NAME',	'DEPT NAME',	'ITEM GROUP NAME',	'ITEM SUB GROUP NAME',	'ITEM NAME',	'COLOR NAME',
                       	'SIZE',	'LOOK NAME',	'USER ITEM CODE',	'HSN CODE',	'ITEM DESC OUR',	'STYLE NAME',	'BASIC RATE',	'PUR RATE',	'SALE RATE',	'OPENING STOCK',
                        'OPENING VALUE(PUR)',	'PURCHASE QTY',	'PURCHASE VALUE',	'PURCHASE RETURN QTY',	'PURCHASE RETURN VALUE',	'NET PURCHASE QTY',
                        'NET PURCHASE VALUE',	'NET SALE QTY',	'NET SALE VALUE(SALE)',	'NET SALE VALUE(AFTER ADJ)',	'CLOSING STOCK',	'CLOSING VALUE(PUR)',
                        	'CLOSING VALUE(SALE)'
]

blue_club_sales_sql = '''INSERT INTO [SDPD].[dbo].[SIS_BC] 
(    [BRAND]
      ,[DATE]
      ,[SITE NAME]
      ,[DIVISION]
      ,[CAT2]
      ,[BILL NO]
      ,[SECTION]
      ,[PRODUCT]
      ,[CODE]
      ,[ITEMDESC6]
      ,[COLOUR]
      ,[SIZE]
      ,[SALE QTY]
      ,[MRPAMT(A)]
      ,[PRMOAMT(B)]
      ,[ITEMDISCOUNTAMT(C)]
      ,[BILLDISCOUNTAMT(D)]
      ,[LPDISCOUNTAMT(E)]
      ,[EXTAXAMT FACTOR(F)]
      ,[Net Amt]
      ,[FileNm]
      ,[Load_TimeStamp]) 

    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    '''

blue_club_stock_sqlq = '''INSERT INTO [INVT].[dbo].[BC_S]
(    [Sitename]
      ,[Section]
      ,[Category2]
      ,[Brand]
      ,[Department]
      ,[Desc4]
      ,[Division]
      ,[Color]
      ,[Stylecode]
      ,[Desc6]
      ,[Size]
      ,[Fit]
      ,[Quantity]
      ,[MRP]
      ,[FileName]
      ,[Date]
      ,[UploadTimestamp]
      ) 

    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    '''

Kapsons_sales_sqlq = '''INSERT INTO SDPD.dbo.SIS_K 
(    [S# NO#]
      ,[COMPANY NAME]
      ,[BILL DATE]
      ,[BILL NO]
      ,[BRAND NAME]
      ,[ITEM GROUP NAME]
      ,[ITEM SUB GROUP NAME]
      ,[ITEM NAME]
      ,[LOT NO]
      ,[USER ITEM CODE]
      ,[LOT CODE]
      ,[COLOR NAME]
      ,[SIZE]
      ,[MRP RATE]
      ,[SALE QUANTITY]
      ,[SALE VALUE]
      ,[SALE RETURN QUANTITY]
      ,[SALE RETURN VALUE]
      ,[NET SALE QUANTITY]
      ,[NET SALE VALUE]
      ,[NET SALE AFTER ADJ]
      ,[SEASON NAME]
      ,[DISCOUNT]
      ,[SPECIAL DISCOUNT]
      ,[OTHER DEDUCTIONS]
      ,[DISC RS]
      ,[OTHER DISCOUNT]
      ,[OTHER BONUS DISCOUNT]
      ,[GIFT COUPON AMOUNT]
      ,[TOTAL DISCOUNT]
      ,[SCHEME NAME]
      ,[TAX TYPE]
      ,[REMARKS1]
      ,[TAX 3]
      ,[TOTAL TAX]
      ,[REMARKS2]
      ,[HSN CODE]
      ,[SPECIAL SCHEME NAME]
      ,[SALE RATE]
      ,[BASIC RATE]
      ,[GIFT VOUCHER AMOUNT]
      ,[FileNm]
      ,[Load_TimeStamp]) 

    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    '''

Kapsons_stock_sqlq = '''INSERT INTO [INVT].[dbo].[KS] 
(    [S# NO#]
      ,[COMPANY NAME]
      ,[SEASON NAME]
      ,[BRAND NAME]
      ,[DEPT NAME]
      ,[ITEM GROUP NAME]
      ,[ITEM SUB GROUP NAME]
      ,[ITEM NAME]
      ,[COLOR NAME]
      ,[SIZE]
      ,[LOOK NAME]
      ,[USER ITEM CODE]
      ,[HSN CODE]
      ,[ITEM DESC OUR]
      ,[STYLE NAME]
      ,[BASIC RATE]
      ,[PUR RATE]
      ,[SALE RATE]
      ,[OPENING STOCK]
      ,[OPENING VALUE(PUR)]
      ,[PURCHASE QTY]
      ,[PURCHASE VALUE]
      ,[PURCHASE RETURN QTY]
      ,[PURCHASE RETURN VALUE]
      ,[NET PURCHASE QTY]
      ,[NET PURCHASE VALUE]
      ,[NET SALE QTY]
      ,[NET SALE VALUE(SALE)]
      ,[NET SALE VALUE(AFTER ADJ)]
      ,[CLOSING STOCK]
      ,[CLOSING VALUE(PUR)]
      ,[CLOSING VALUE(SALE)]
      ,[UploadTimestamp]
      ,[Date]
      ,[FileName]) 

    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    '''


Lifestyle_sales_sqlq = '''INSERT INTO [SDPD].[dbo].[SIS_LS]
(    [RunDate]
      ,[Date]
      ,[LOC_NUM]
      ,[LOCATION_NAME]
      ,[ITEM]
      ,[EAN_CODE]
      ,[ITEM_DESC_SECONDARY]
      ,[SHORT_DESC]
      ,[DIV_NAME]
      ,[DEPT_NAME]
      ,[CLASS_NAME]
      ,[SUB_NAME]
      ,[BRAND_DESC]
      ,[SUP_NAME]
      ,[COLOR_DESC]
      ,[SIZE_DESC]
      ,[Sum_of_QTY]
      ,[Sum_of_SALRRP]
      ,[Sum_of_TAX]
      ,[Sum_of_SALNOT]
      ,[Sum_of_SALMRP]
      ,[FileNm]
      ,[Load_TimeStamp]) 

    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
)

    '''

Lifestyle_stock_sqlq = sqlq = '''INSERT INTO [INVT].[dbo].[LS_S]
(    [RUNDATE]
      ,[SUP_NAME]
      ,[LOC_NUM]
      ,[LOC_NAME]
      ,[DIV_NAME]
      ,[DEPT_NAME]
      ,[BRAND_DESC]
      ,[CLASS_NAME]
      ,[SUB_NAME]
      ,[ITEM]
      ,[ITEM_DESC]
      ,[EAN]
      ,[SHORT_DESC]
      ,[ITEM_DESC_SECONDARY]
      ,[COLOR_DESC]
      ,[SIZE_DESC]
      ,[MRP]
      ,[CLSQTY]
      ,[GITQTY]
      ,[UploadTimestamp]
      ,[Date]
      ,[FileName]) 

    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    '''

shoppers_sales_sqlq = '''INSERT INTO [SDPD].[dbo].[SIS_S] 
(    [COLUMN1]
      ,[PARTNER]
      ,[LOCATION_]
      ,[STYLE_CODE]
      ,[STYLE_DESC]
      ,[HSN_CODE]
      ,[SKU_NO]
      ,[BARCODE_SCANNED_FOR_BILLING]
      ,[GS1_NUMBER]
      ,[SELLING_DATE]
      ,[BRAND_NAME]
      ,[CATEGORY]
      ,[SUB_CATEGORY]
      ,[PARTNER_PART_NO]
      ,[COLOUR_DESC]
      ,[SIZE_DESC]
      ,[Sum_of_QTY_SOLD]
      ,[Sum_of_ACTUAL_RETAIL_VALUE]
      ,[Sum_of_DISC_AMT]
      ,[Sum_of_NET_RETAIL_VALUE]
      ,[IS_AUDITED]
      ,[FileNm]
      ,[Load_TimeStamp]) 

    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    '''

shoppers_stock_sqlq = '''INSERT INTO [INVT].[dbo].[SS_S] 
(    Partner
    ,Location
    ,Style_Code
    ,Style_Desc
    ,Season
    ,HSN_Code
    ,SKU_No
    ,GS1_NUMBER
    ,Brand
    ,Category
    ,Sub_Category
    ,Partner_Part_No
    ,Color_Desc
    ,Size_Desc
    ,Qty_Available
    ,Actual_Retail_Value
    ,UploadTimestamp
    ,Date
    ,FileName) 

    values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    '''

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
    if "Itemwise" not in filename[0]:
        fname_list = covert_to_csv(filename, csv_location)
    else: fname_list = filename
    dfs = []
    for f, t in zip(fname_list, ftd):
        # if "Stock_KPBS" in f:
        #     df = pd.read_csv(f, index_col=None, dtype=dtype, header=4, parse_dates=parse_date, dayfirst=dayfirst, encoding=encoding)
        # else:
        #     # print(f)
        if f.split("\\")[-1].split('.')[0] in [f"StockReport({x})" for x in range(6,15)] or "SaleReport(4).xls" in f:
            df = pd.read_csv(f, index_col=None, dtype=dtype, header=3, parse_dates=parse_date, dayfirst=dayfirst, encoding=encoding)
        else: df = pd.read_csv(f, index_col=None, dtype=dtype, header=header, parse_dates=parse_date, dayfirst=dayfirst, encoding=encoding)
        if "Sales" in partner:
            if "Kapsons" in partner or "Shoppers" in partner:
                df.drop(df.tail(1).index,inplace=True)
            if "Kapsons" in partner:
                if "SaleReport(4).xls" in f:
                    df['LOT NO'] = df['LOT NO'].str.replace("/\d+", '', regex=True)
                    df.insert(len(df.columns), 'OTHER DEDUCTIONS', '0')
                    df.insert(len(df.columns), 'DISC RS', '0')
                    df.insert(len(df.columns), 'OTHER BONUS DISCOUNT', '0')
                    df.insert(len(df.columns), 'GIFT COUPON AMOUNT', '0')
                    # df.insert(len(df.columns), 'SCHEME NAME', '')
                    df.insert(len(df.columns), 'TAX 3', '0')
                    df.insert(len(df.columns), 'TOTAL TAX', '0')
                    # df.insert(len(df.columns), 'SPECIAL SCHEME NAME', '')
                    df.insert(len(df.columns), 'BASIC RATE', '0')
                    df.insert(len(df.columns), 'GIFT VOUCHER AMOUNT', '0')
                    df = df[kp_bs_sales_columns]
                else:
                    df = df.drop(['GIFT COUPON NAME', 'MOBILE SCHEME MOBILE NUMBER', 'OTHER BONUS DISCOUNT BRAND', 'OTHER BONUS DISCOUNT COMPANY', 'OTHER DISCOUNT BRAND', 'OTHER DISCOUNT COMPANY'], axis=1)
                    df.insert(26, 'OTHER DISCOUNT', '0')
                    df.insert(27, 'OTHER BONUS DISCOUNT', '0')
                    SSN = df.pop('SPECIAL SCHEME NAME')
                    df.insert(37, SSN.name, SSN)
                a = list(df['LOT NO'][~df['LOT NO'].str.isdigit()].index)
                for b in a:
                    df.at[b, 'LOT NO'] = '0'
                print(list(df.columns))
            if "Shoppers" in partner:
                df = df.drop(['Distribution\nChannel', 'Store No.'], axis=1)
            # print(list(df.columns))
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
                    if f.split("\\")[-1].split('.')[0] in [f"StockReport({x})" for x in range(6,15)]:
                        df.insert(len(df.columns), 'LOOK NAME', '')
                        df.insert(len(df.columns), 'ITEM DESC OUR', '')
                        df.insert(len(df.columns), 'STYLE NAME', '')
                        df.insert(len(df.columns), 'PUR RATE', 0)
                        df.insert(len(df.columns), 'PURCHASE RETURN VALUE', 0)
                        df.insert(len(df.columns), 'BASIC RATE', 0)
                        df.insert(len(df.columns), 'SALE RATE', 0)
                        df.insert(len(df.columns), 'PURCHASE VALUE', 0)
                        # print(df.columns)
                        df = df[kp_bs_stock_columns]
                    else:
                        df.drop(df.tail(1).index,inplace=True)
                if "Shoppers" in partner:
                    df.drop(['Store No.'], axis=1, inplace=True)
                    if "StockDetails.xlsx" in f or 'Stock_SS_HR' in f:
                        df = HR_filter(df)
                # print(list(df.columns))
                df['UploadTimestamp'] = pd.to_datetime('now').replace(microsecond=0)
                df['Date'] = t
                df['FileName'] = f.split("\\")[-1]
        dfs.append(df)
    sqlq = f"delete from {table} "
    cursor.execute(sqlq)
    cursor.commit()
    all_df = pd.concat(dfs, ignore_index=True)
    all_df = all_df.fillna('')
    # print(all_df)
    # print(all_df.columns)
    # print(all_df.dtypes)
    # print(len(all_df.columns))
    # return all_df
    cursor.fast_executemany = True
    df_list = all_df.values.tolist()
    for i in range(0, len(df_list), 25000):
        cursor.executemany(sqlqi, df_list[i:i + 25000])
        print(i)
        cursor.commit()
    print(len(df_list))
    cursor.close()


loading(Kapsons_sales, "Kapsons_Sales", "SDPD.dbo.SIS_K", connection.cursor(),
         Kapsons_sales_sqlq, str, 3, encoding='ansi')

loading(Kapsons_stock, "Kapsons_Stock", "[INVT].[dbo].[KS] ", connection.cursor(),
        Kapsons_stock_sqlq, str, 4)

loading(Blue_club_sales, "Blue Club_Sales", "[SDPD].[dbo].[SIS_BC]", connection.cursor(),
        blue_club_sales_sql, BC_sales_datatype, 0, parse_date=['DATE'], dayfirst=True)

loading(Lifestyle_sales, "Lifestyle_Sales", "[SDPD].[dbo].[SIS_LS]", connection.cursor(),
       Lifestyle_sales_sqlq, str, 0)

loading(Lifestyle_stock, "Lifestyle_Stock", "[INVT].[dbo].[LS_S]", connection.cursor(),
       Lifestyle_stock_sqlq, str, 0)

loading(Shoppers_sales, "Shoppers_Sales", "[SDPD].[dbo].[SIS_S]", connection.cursor(),
       shoppers_sales_sqlq, str, 4)

loading(Shoppers_stock, "Shoppers_Stock", "[INVT].[dbo].[SS_S]", connection.cursor(),
       shoppers_stock_sqlq, str, 3)



connection.close()



