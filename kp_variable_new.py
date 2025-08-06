'''File contaning function to check existence of files and define filepaths

2 functions:
    - fnames
    - checkfiles

The checkfiles function uses the fnames function to get fullpaths
folder names are passed in the function to get list of fullpath
'''

import shutil
import glob, os
from datetime import date as dt
from datetime import timedelta
import re

csv_location=r"D:\Files\Input\KP_Backup\csv"

csv_list = glob.glob(r"D:\Files\Input\KP_Backup\csv\*")
for c in csv_list:
    os.remove(c)

td = dt.today()
yt = td - timedelta(days = 1)
ytd = yt.strftime("%d.%m.%Y")
ytdmy = yt.strftime("%d-%m-%Y")
ytymd = yt.strftime("%Y-%m-%d")
tdymd = td.strftime("%Y-%m-%d")
tddmy = td.strftime("%d-%m-%Y")

kp_location = r"\\BOT\Robotics_Automation\SIS\SIS_Report"+"\\"+tddmy

def fnames(folder: str, kp_location:str=kp_location) -> list:
    '''Get full path of the sale and stock files

    Parameters:
        folder: folder name to look in
        kp_location: fullpath of the location of folder

    Returns:
        Sales: list of fullpath of files containing sales
        Stock: list of fullpath of files containing stock
    '''
    fl = os.listdir(kp_location+"\\"+folder)
    sales = {re.sub("\d+\.[a-zA-Z]+", "", i):i for i in fl if i.startswith("Sales")}
    stock = {re.sub("\d+\.[a-zA-Z]+",  "", i):i for i in fl if i.startswith("Stock")}
    return sales, stock

bk_location=r"D:\Files\Input\KP_Backup"

def checkfiles(folder: str) -> list:
    '''use the fnames to check existence of files downloaded from robotics. If a particular file is not there, use the backup file. If it's there then copy the file to backup folder

    Parameters:
        folder: Name of the folder where files are

    Returns:
        Sales: list of fullpath of files containing sales
        Stock: list of fullpath of files containing stock
    '''
    bk_location=r"D:/Files/Input/\KP_Backup"
    if not os.path.exists(kp_location):
        old_sales, old_stock = fnames(folder, bk_location)
        return old_sales, old_stock
    new_sales, new_stock = fnames(folder)
    old_sales, old_stock = fnames(folder, bk_location)
    def check(x, y):
        files = []
        for a in y.keys():
            if a in x.keys():
                if folder == "Blueclub" and os.path.getsize(kp_location+"\\"+folder+"\\"+x[a]) == 8462:
                    files.append(bk_location+"\\"+folder+"\\"+y[a])
                    continue
                os.remove(bk_location+"\\"+folder+"\\"+y[a])
                shutil.copyfile(kp_location+"\\"+folder+"\\"+x[a], bk_location+"\\"+folder+"\\"+x[a])
                files.append(bk_location+"\\"+folder+"\\"+x[a])
                print(a)
            else: files.append(bk_location+"\\"+folder+"\\"+y[a])
        return files
    sales = check(new_sales, old_sales)
    stock = check(new_stock, old_stock)
    return sales, stock

Blue_club_sales, Blue_club_stock = checkfiles("Blueclub")

Kapsons_sales, Kapsons_stock = checkfiles("Kapsons")

Lifestyle_sales, Lifestyle_stock = checkfiles("Lifestyle")

Shoppers_sales, Shoppers_stock = checkfiles("Shoppers Stop")

_ , Shoppers_stock_JJ = checkfiles("Shoppers Stop\\JJ1")

_ , Shoppers_stock_ON = checkfiles("Shoppers Stop\\ON")

_ , Shoppers_stock_VM = checkfiles("Shoppers Stop\\VM")

all_shopeprs_stock = Shoppers_stock+Shoppers_stock_JJ+Shoppers_stock_ON+Shoppers_stock_VM

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

blue_club_sales_sql = '''INSERT INTO [SDPD].[dbo].[SIS_BCB] 
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