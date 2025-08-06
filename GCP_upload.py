import sql_con
import variable
import logging
import GCP_queries
import pandas as pd
from datetime import date as dt
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
import random

def log(flnm: str):
    fullname = variable.GCP_log_loc+flnm+".log"
    logging.basicConfig(level=logging.INFO, filename=fullname, filemode='w', format='%(asctime)s -- %(levelname)s -- %(message)s')
    return logging

logging = log('script')
print("Starting")
database = "FACT"
connection = sql_con.get_con(database)
today_date = variable.tddmy_

logging.info("Fetching changes")
print("Fetching changes")
old_data, new_data = GCP_queries.data_tracker(connection)

def normalize(l):
    rows = []
    for row in l:
        rows.append(tuple(row))
    return rows

columns = ['rundate',	'EOM',	'Channel',	'Sales',	'Target_ABP',	'Target_Field',	'Target_Margine',	'Stock']

df1 = pd.DataFrame(normalize(old_data), columns=columns)
df2 = pd.DataFrame(normalize(new_data), columns=columns)
new = df1.merge(df2, how='outer', on=['EOM', 'Channel'])

new.fillna(0, inplace=True)

logging.info("calculating changes")
print("calculating changes")
new['diff_sales'] = new['Sales_y'] - new['Sales_x']
new['diff_ABP'] = new['Target_ABP_y'] - new['Target_ABP_x']
new['diff_Field'] = new['Target_Field_y'] - new['Target_Field_x']
new['diff_GM'] = new['Target_Margine_y'] - new['Target_Margine_x']
new['diff_stock'] = new['Stock_y'] - new['Stock_x']

sales = new[new['diff_sales'].notnull()][(new['diff_sales'] > 1) | (new['diff_sales'] < -1)]
abp = new[new['diff_ABP'].notnull()][(new['diff_ABP'] > 1) | (new['diff_ABP'] < -1)]
field = new[new['diff_Field'].notnull()][(new['diff_Field'] > 1) | (new['diff_Field'] < -1)]
gm = new[new['diff_GM'].notnull()][(new['diff_GM'] > 0) | (new['diff_GM'] < -1)]
stock = new[new['diff_stock'].notnull()][(new['diff_stock'] > 1) | (new['diff_stock'] < -1)]

def changes(df, data):
    ls = df[['EOM', 'Channel']].values.tolist()
    dt = []
    for e, c in ls:
        end_date = e.strftime("%Y-%m-%d")  
        e = e.replace(day=1)
        start_date = e.strftime("%Y-%m-%d")
        if data == 'Sales':
            if c == 'Online_captive': filnm = GCP_queries.filenames['Online']
            elif c == 'SIS': filnm = GCP_queries.filenames['SIS_Man']
            elif c == 'SIS_Articlewise': filnm = GCP_queries.filenames['SIS_M']
            elif c == 'Online Outright': filnm = GCP_queries.filenames['Online_OR']
            elif c in 'Distribution': filnm = GCP_queries.filenames['Outright_UG']
            elif c in 'Distribution SOR':
                cursor = connection.cursor()
                cursor.execute(f" select Upload_mth from FACT.dbo.S_PCN where BILLDate >= '{start_date}' and BILLDate <= '{end_date}'")
                dsor = cursor.fetchall()
                if dsor[0][0] == 'Manual': filnm = GCP_queries.filenames['Panchanan_M']
                else: filnm = GCP_queries.filenames['Panchanan']
            else: filnm = False
        elif data == 'Target':
            if c == 'SIS': filnm = GCP_queries.filenames['SIS_Target']
            elif c == 'Online': filnm = GCP_queries.filenames['Online_target']
            elif c == 'Online Omni': filnm = GCP_queries.filenames['Online_Omni']
            elif c == 'POS': filnm = GCP_queries.filenames['POS_Target']
            elif c == 'Captive_Omni': filnm = GCP_queries.filenames['Captive_Omni']
            else: filnm = False
        elif data == 'Stock':
            if c == 'Online_captive': filnm = GCP_queries.filenames['Online_Stock']
            elif c == 'SIS': filnm = GCP_queries.filenames['SIS_Stock']
            else: filnm = False
        dt.append({'type': data, 'start_date': start_date, 'end_date': end_date, 'Channel': c, 'Filnm': filnm})
    return dt


targets = changes(abp, 'Target') + changes(field, 'Target') + changes(gm, 'Target')
removed_duplicate = []
for target in targets:
    if target not in removed_duplicate:
        removed_duplicate.append(target)
    else:
        continue

Stock = changes(stock, 'Stock')
stock = []
s = []
for i in Stock:
    if i['Channel'] not in s:
        stock.append(i)
        s.append(i['Channel'])

data_to_upload = changes(sales, 'Sales') + removed_duplicate + stock
# data_to_upload = stock
logging.info("data to upload: "+str([(i['type'], i['Channel'], i['start_date'], i['end_date']) for i in list(data_to_upload)]))
print("sales data to upload: ", [(i['type'], i['Channel'], i['start_date'], i['end_date']) for i in list(data_to_upload)])

def ETL(d, today_date):
    today_date = today_date+'_'+''.join(random.choice('0123456789ABCDEF') for i in range(6))
    if d['type'] == 'Stock':
        filename = GCP_queries.save_data(d['Filnm']['query'], d['Filnm']['file'], today_date, connection)
        new_filename = filename
    else:
        filename = GCP_queries.save_data(d['Filnm']['query'].format(d['start_date'], d['end_date']), d['Filnm']['file'], today_date, connection)
        new_filename = GCP_queries.convert_excel(filename, d['Filnm']['format'])
    GCP_queries.file_transfer(new_filename)

logging.info("uploading")

for d in data_to_upload:
    if d['Filnm'] == False:
        continue
    ETL(d, today_date)

connection.close()



