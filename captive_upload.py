import auth
import pyodbc
import csv
import win32com.client
import variable
from google.cloud import storage

database = "FACT"
connect_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=host;'
connect_string += f'DATABASE={database};UID={auth.usr};PWD={auth.ps}'
connection = pyodbc.connect(connect_string)

from_date = variable.lmfd

Online_sales = f'''select [Date], Ean, Generic, o.Article, E.Style as BI2, Brand_As_per_Master, description, Cat, Store_code, Store_Name, Partner, City_ as city,
sum(Sum_of_Sales_Amt) as Sales_amt_after_40_percen_return, sum([Sales_Amt_100%]) as Sales_amt, MRP_as_per_Master, sum([Sales_QTY_100%]) as _Sale_QTY_,
sum(Sum_of_Sale_QTY) as _Sales_qty_after_40_percen_return_, o.season as _Season_, o.size as _Size_, o.color as _color_, Region as _Region_, MRP_as_per_Partner, null as Remark_1, sum(Sum_of_Sales_Amt/nullif(Sum_of_Sale_QTY, 0)) as ASP,
null as Remark_2, null as Bill_No, null as Ean, null as ART, null as BI2_1, null as Article_1, null as BI2_No_1, null as brand_as_per_Partner, null as Store_Name_1, null as Partner_1, null as con,
 null as ug_art,  null as pre_art,  null as shoes,  null as Old_code, null as Code_Con, Map, sum(Unit_cost) as Unit_cost, sum(Margin_value) as Margin_value, null as Con_cat, null as Tax_percentage,
 sum(Tax_amt) as Tax_amt, sum(Net_Margin) as Net_Margin, sum(MRP_Value) as MRP_Value
from FACT.dbo.[sales_in_channel_online] o
left outer join DIM.dbo.article E
on o.Article = E.Article
where date >= '{from_date}'
group by
[Date], Ean, Generic, O.Article, E.Style, Brand_As_per_Master, description, Cat, Store_code, Store_Name, Partner, City_, 
[MRP_as_per_Master]
	  ,o.Season	
      ,o.size
      ,o.color
      ,Region
      ,[MRP_as_per_Partner]
	  ,[MAP]


'''

today_date = variable.tddmy_+'_0'
def fetch_data(query, fname):
    cursor=connection.cursor()
    sqlq = query
    filename = variable.uploads+fname+today_date+".csv"
    wh = open(filename, 'w', encoding='utf-8', newline='')
    csvw = csv.writer(wh)
    cursor.execute(sqlq)
    columns = [column[0] for column in cursor.description]
    csvw.writerow(columns)
    print("fetching")
    rows = cursor.fetchall()
    print("Writting")
    csvw.writerows(rows)
    wh.flush()
    wh.close()
    cursor.close()
    return filename

def convert_excel(fname, fformat):
    excel = win32com.client.Dispatch("Excel.Application")
    doc = excel.Workbooks.Open(fname)
    newname = fname.replace("csv", fformat)
    if fformat == 'xlsb': ff = 50
    else: ff = 51
    excel.Application.DisplayAlerts = False 
    doc.SaveAs(newname, ff, )
    doc.Close(SaveChanges=False)
    excel.Application.Quit()
    return newname

filename = fetch_data(Online_sales, 'Online_sales_')
print(filename)
win_file = filename.replace('/', '\\')
filename = convert_excel(win_file, 'xlsb')
binary_file = filename.replace('\\', '/')

connection.close()

def file_transfer(filename):
    client = storage.Client.from_service_account_json("GCP_service.json")
    bucket = storage.Bucket(client, 'bucket_name')
    fn = filename.split('/')[-1]
    blob = bucket.blob(f'folder/{fn}')
    blob.upload_from_filename(filename)
    print('Uploaded', fn)

file_transfer(binary_file)


