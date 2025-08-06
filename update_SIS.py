import queries
import process_data
import procedure
import os
import variable
import datetime as dt
import pandas as pd
import sql_con


def sis(conx: object, channel_table: dict, filenm: list) -> None:
    '''Update SIS data

    Parameters:
        conx: Database object
        channel_table: channel and table details
        filenm: list containing filenames

    Returns:
        None
    '''
    if not os.path.exists(variable.location+"\\"+filenm[0]):
        exit()
    procedure.starting(conx, channel_table, 'truncate')
    df = process_data.get_data(filenm)
    print(len(df))
    # df = pd.read_excel(variable.location+"\\"+filenm[0], dtype=str, encoding="ansi")
    df['real_date'] = pd.TimedeltaIndex(pd.to_numeric(df['Date']), unit='D') + dt.datetime(1899, 12, 30)
    start_date = df['real_date'].min().strftime('%d-%m-%Y')
    print("Start Date:", start_date)
    start_date = df['real_date'].min().strftime('%Y-%m-%d')
    print("End Date:", df['real_date'].max().strftime('%d-%m-%Y'))
    if input("Please confirm the date abaove. Enter to accept. n to reject and exit: ") == 'n':
        exit()
    df['real_date'] = df['real_date'].dt.strftime('%d-%m-%Y')
    sales_df = df[channel_table['columns']].copy()
    total = sales_df.sum(numeric_only=True)
    for k, v in total.to_dict().items():
        print(k,'\t:\t',v)
    sales_df = sales_df.values.tolist()
    sales_df = procedure.fill_null(sales_df)
    process_data.sql_insert(sales_df, queries.manual_sis, cursor=conx.cursor())
    return start_date

conx = sql_con.get_con('SSF')

fn = []
fdir = os.listdir(variable.location)
for i in fdir:
    if "XLSX" in i:
        fn.append(i)

start_date = sis(conx, queries.sis_sales, fn)

cursor=conx.cursor()
q = " select max(date) from FACT.dbo.S_SIS where upload_mth not like '%Man%' "
cursor.execute(q)
date = cursor.fetchall()
date = date[0][0].strftime('%Y-%m-%d')

q = f" EXEC [FACT].[dbo].[Sales_Manual_SIS]  @InitialDate = '{start_date}',@FinalDate = '{date}' "
print(q)
if input("proceed: ") != '':
    exit()
cursor.execute(q)

q = f'''
select eomonth(date) as monthdate,sum([Sales_amt]) as Sales_amt,sum([Sale_QTY]) as Sale_QTY,sum([Net_Margin]) as Net_Margin
from FACT.dbo.S_SIS where Date >= '{start_date}'
group by eomonth(date)
order by eomonth(date)
'''
cursor.execute(q)
result = cursor.fetchall()
columns = [column[0] for column in cursor.description]
print(columns)

for row in result:
    print(row)

cursor.close()

conx.close()