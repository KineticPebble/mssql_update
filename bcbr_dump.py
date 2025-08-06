import time
start_time = time.time()
import pandas as pd
import sql_con
from datetime import date
import os, glob
import procedure
from sftpop import sftp
import variable

sftp.connect()
download_loc = 'D:/Files/Input/bcbr_main/'
source_loc = 'main'
td = variable.tddmy_
SP = 'exec [PROD].[dbo].[BCBR_INSERT]'

old_file = glob.glob(download_loc+"/*")
for c in old_file:
    os.remove(c)

def get_latest():
    ls = sftp.listdir(source_loc)
    for i in ls:
        if f"BCBR_{td}.csv" in i:
            return i
    print("File not found")
    sftp.disconnect()
    exit()

target_file = get_latest()
sftp.download(source_loc+"/"+target_file, download_loc+"/"+target_file)
sftp.disconnect()

database = "PROD"
connection = sql_con.get_con(database)

dates = ['Date_of_Order_Generated', 'Shipping_Date', 'Invoice_Date', 'Shipment_Delivered_Date', 'Dispatch_Date', 'RTO_Initiated_Date', 'RTO_Delivered_Date',
          'RTV_Initiated_Date', 'RTV_Delivered_Date']

df = pd.read_csv(download_loc+"/"+target_file, parse_dates=dates, dayfirst=False)
df['Time_of_Order_Generated'] = pd.to_datetime(df['Time_of_Order_Generated'], format="%I:%M:%S %p").dt.strftime("%H:%M:%S")

cl = ['Order_ID',	'OrderLineNo',	'MP_Order_ID',	'MP_Sub_OrderID',	'Consignment_Id',	'Sap_Style_Id',	'Style_Id',	'EAN_Code',	'Product_Detail',	'Item_Description',
      	'Product_Size',	'Order_Type',	'Brand',	'Sub_Brand',	'Date_of_Order_Generated',	'Time_of_Order_Generated',	'Shipping_Date',	'storepickup',	'Invoice_Date',	
        'Ordering_Store_Sap_Code',	'Ordering_Store_Name',	'Ordering_Store_City',	'Fulfilling_Store_SAP_Code',	'Fulfilling_Store',	'Fulfilling_Store_City',	'FF_Flag',	
        'Return_Source',	'Mode_of_Delivery',	'Mode_of_Delivery1',	'Delivery_Location_City',	'Store_UserName',	'Store_Agent',	'Customer_Email',	'ExternalBrandInvoiceNo',	
        'Promotion_Description',	'Promotion_Name',	'AWB',	'Fulfillment_Type',	'Courier_Name',	'Shipment_Delivered_Date',	'Dispatch_Date',	'RTO_Initiated_Date',	
        'RTO_Delivered_Date',	'Return_id',	'RTV_Initiated_Date',	'RTV_Delivered_Date',	'Return_Type',	'RTV.couriername',	'RTV.awb',	'Payment_Mode',	'LMS_Status',	
        'OMS_Status',	'Order_Status',	'GMV',	'Orderline_Discount',	'NMV',	'Taxes',	'Quantity',	'Orders',	'Article_Description',	'ARM_Mapping',	'Region_Mapping',	
        'Upload Date',	'Customer_Destination_Pincode', 'timestamp'
]

df['Upload Date'] = pd.to_datetime("today").date()
df['timestamp'] = pd.to_datetime('now').replace(microsecond=0)

df = df[cl]

bcbr = ''' INSERT INTO [PROD].[dbo].[Main_BCBR_SSIS]

      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

sqldq = f"delete from [PROD].[dbo].[Main_BCBR_SSIS]"
cursor = connection.cursor()
cursor.execute(sqldq)
cursor.commit()

all_df = df.fillna('')
df_list = all_df.values.tolist()
all_df = procedure.fill_null(df_list)
all_df = procedure.fill_NaT(df_list)
cursor.fast_executemany = True
for i in range(0, len(df_list), 25000):
    cursor.executemany(bcbr, df_list[i:i + 25000])
    print(i)
    cursor.commit()
print(len(df_list))
cursor.close()

print("running SP")
os.system(f'''cmd /c sqlcmd -Q " {SP} " -o "D:\SAP_files\Logs\Validation\\bcbr_main.csv" -s "," ''')
print("--- %s seconds ---" % (time.time() - start_time))