from google.cloud import storage
import win32com.client
import variable
import csv

ls = ['SIS_Man', 'SIS_M', 'SIS_W', 'Online', 'Online_NS', 'Online_OR', 'Outright_UG', 'PCN', 'PCN_M']

SIS_M_Sales = '''   Query for SIS_M sales
   '''

Online_sales = ''' Query for Online Sales

'''

data_tracker_q = ''' select GETDATE() as rundate, isnull(s.EOM, t.EOM), isnull(s.Channel, t.Channel), cast(s.Sales as bigint) as Sales, cast(t.ABP_Target as bigint) as Target_ABP,
cast(t.Field_Target as bigint) as Target_Field, cast(t.GM_Target as bigint) as Target_Margine, cast(st.Stock as bigint) as Stock from
(select EOMONTH(Date) as EOM, Channel, sum(Sales_amt) as Sales from [FACT].dbo.S_SIS
where date >= '2023-08-01'
group by EOMONTH(Date), Channel
union all
select EOMONTH(Date) as EOM, 'SIS_A' as Channel, sum(Sales_amt) as Sales from [FACT].dbo.S_SIS
where date >= '2023-08-01'
and Upload_Mth not like 'Man%'
group by EOMONTH(Date)
union all 
select EOMONTH(Date) as EOM, 'Online_captive', sum(Sum_of_Sales_Amt) as Sales from [FACT].dbo.SON
where date >= '2023-08-01'
group by EOMONTH(Date)
union all
select EOMONTH(date) as EOM, 'Distribution', sum([Sales_iV]) as Sales from FACT.dbo.outright_M
where date >= '2023-08-01'
group by EOMONTH(Date)
union all
select EOMONTH(Date) as EOM, Channel, sum(Sum_of_Sales_Amt) as Sales from FACT.dbo.SON_Outright
where date >= '2023-08-01'
group by EOMONTH(Date), Channel
union all
select EOMONTH(BILLDate) as EOM, 'Distribution SOR' as channel, sum([NET SALE VALUE]) as Sales from FACT.dbo.Sales_PCN
where BILLDate >= '2023-08-01'
group by EOMONTH(BILLDate)
) s

full outer join

(select EOM, channel, sum(ABP_Target) as ABP_Target , sum(Field_Target) as Field_Target, sum(GM_Target) as GM_Target
from 
(select  EOMONTH(DATE) as EOM,
case when Channel in ('Captive', 'Online', 'Online Outright') then 'Online'
when Channel in ('EBO', 'MBF') then 'POS' else Channel
end as Channel, sum(ABP_Target) as ABP_Target , sum(Field_Target) as Field_Target, sum(GM_Target) as GM_Target from FACT.dbo.Targets 
where date >= '2023-08-01'
group by EOMONTH(DATE), Channel) tt
group by EOM, channel
) t
on s.EOM = t.EOM and s.Channel = t.Channel
left outer join 
(select  EOMONTH(convert(date,[date],104)) as EOM, 'Online_captive' as Channel, sum(cast([StockQty ] as int)) as Stock from [Stock].[dbo].[Online_Stock]
group by EOMONTH(convert(date,[date],104))
union all
select EOMONTH(convert(date,[date],104)) as EOM, 'SIS' as Channel, sum(cast(StockQty as int)) as Stock from [Stock].[dbo].[SIS_Stock]
group by EOMONTH(convert(date,[date],104))
) st
on s.Channel = st.Channel and s.EOM = st.EOM
order by s.EOM, s.Channel


 '''

SIS_A = ''' SQL query to extract SIS_A
'''

Outright_UG = ''' SQL query to extract Outright_UG
'''

Online_OR = ''' SQL query to extract Online_OR
'''

PCN = ''' SQL query to extract PCN
'''

PCN_Man = ''' SQL query to extract PCN_Man
  '''

SIS_Target = ''' SQL query to extract sis
'''

POS_Target = ''' SQL query to extract pos
'''

Online_target = ''' SQL query to extract online
'''

Online_Omni = ''' SQL query to extract omni
'''

Captive_Omni = ''' SQL query to extract captive
'''

Online_Stock = ''' SQL query to extract online stock
      '''

SIS_Stock = ''' SQL query to extract sis stock
'''

filenames = {'SIS_Man': {'file':'SIS_Manual_Sales_', 'format': 'xlsx', 'query': SIS_M_Sales}, 'SIS_M': {'file':'SIS_A_Monthly_', 'format': 'xlsb', 'query': SIS_A},
             'SIS_W': {'file':'SIS_A_Weekly_', 'format': 'xlsb', 'query': SIS_A}, 'Online': {'file':'Online_Articlewise_', 'format': 'xlsb', 'query': Online_sales},
             'Online_NS': {'file':'Online_Articlewise_Net_Sales_',  'format': 'xlsb', 'query': Online_sales}, 'Online_OR': {'file':'Online_OR_Articlewise_',  'format': 'xlsb', 'query': Online_OR},
             'Outright_UG': {'file':'UG_Distribution_Articlewise_',  'format': 'xlsx', 'query': Outright_UG}, 'PCN': {'file':'Distribution SOR ArticleWise_',  'format': 'xlsx','query': PCN},
             'PCN_M': {'file':'Distribution SOR Manual_',  'format': 'xlsx', 'query': PCN_Man}, 'SIS_Target': {'file':'SIS Target_',  'format': 'xlsb','query': SIS_Target},
             'POS_Target': {'file':'EBO-FRANCHISEE-TDR TARGET_',  'format': 'xlsb', 'query': POS_Target}, 'Online_target': {'file':'Online Target_',  'format': 'xlsb','query': Online_target},
             'Online_Omni': {'file':'Myntra Omni_',  'format': 'xlsb', 'query': Online_Omni}, 'Captive_Omni': {'file':'Captive Omni_',  'format': 'xlsb', 'query': Captive_Omni},
             'Online_Stock': {'file':'Online stock report_',  'format': 'csv', 'query': Online_Stock}, 'SIS_Stock': {'file':'SIS stock report_',  'format': 'csv', 'query': SIS_Stock}}


def data_tracker(connection):
    cursor=connection.cursor()
    sql_q = '''select * from [FACT].[dbo].[Data_tracker]
    where rundate = (select max(rundate) from [FACT].[dbo].[Data_tracker]
    ) order by EOM, channel '''
    cursor.execute(sql_q)
    rows1 = cursor.fetchall()
    sqlq = '''EXEC [FACT].[dbo].[Data_Tracker_SP] '''
    cursor.execute(sqlq)
    cursor.commit()
    cursor.execute(sql_q)
    rows2 = cursor.fetchall()
    cursor.close()
    return rows1, rows2


def save_data(query, fname, today_date, connection):
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
    fname = fname.replace('/', '\\')
    doc = excel.Workbooks.Open(fname)
    newname = fname.replace("csv", fformat)
    if fformat == 'xlsb': ff = 50
    else: ff = 51
    excel.Application.DisplayAlerts = False 
    doc.SaveAs(newname, ff, )
    doc.Close(SaveChanges=False)
    excel.Application.Quit()
    newname = newname.replace('\\', '/')
    return newname

def file_transfer(filename):
    client = storage.Client.from_service_account_json("GCP_service.json")
    bucket = storage.Bucket(client, 'bestseller-prod-raw')
    fn = filename.split('/')[-1]
    blob = bucket.blob(f'mis/{fn}')
    blob.upload_from_filename(filename)
    print('Uploaded', fn)



