
import time
start_time = time.time()
import sql_con
import queries
import variable
import os
import process_data
import procedure
import pandas as pd
from hdbcli import dbapi

def get_vbrp():
    conn = dbapi.connect(
        address="address",
        port=30013,
        user="user",
        password="password",
        databasename='111'
    )
    cursor = conn.cursor()

    fh = open(variable.location+"\\"+"all_BD.csv", encoding='utf-8')
    bd = []
    for line in fh:
        line = line.strip()
        if line != '0':
            bd.append(line)
    bd = str(bd)[1:-1]

    sql_query = f'''  SELECT VKORG, FKDAT,	VTWEG,	FKART,	KUNNR,	KUNAG,	VBTYP,	ERNAM,	VBELN,	FKIMG,	VBELV,	ARKTX,	MATNR,	EANNR,	ERDAT,	ERZET,	KZWI1,	KZWI2,	KZWI3,	KZWI4,	KZWI5,	KURSK,	EAN11,	PRCTR,	MWSBP,	BRTWR,	NETWR,	SHKZG  
    FROM 111.VBRP
    WHERE 
    VBELN  in ({bd}) '''

    cursor.execute(sql_query)
    print('fetching')
    rows = cursor.fetchall()

    columns = ['SOrg.',	'Billing Date',	'DChl',	'BillT',	'Payer',	'Sold-To Pt',	'DocCa',	'Created By',	'Bill.Doc.',	'Billed Quantity',	'OriginDoc.',	'Description',	'Material',	'EAN number',	'Created On',	'Time',	'Subtotal 1',	'Subtotal 2',	'Subtotal 3',	'Subtotal 4',	'Subtotal 5',	'Exch.Rate',	'EAN/UPC',	'Profit Ctr',	'Tax amount',	'Gross value',	'Net value',	'Ret']
    df = pd.DataFrame(rows)
    df.columns = columns
    return df

def insert_into(conx: object, channel_table: dict, filenm: list) -> None:
    '''Update SAP data

    Parameters:
        conx: Database object
        channel_table: channel and table details
        filenm: list containing filenames

    Returns:
        None
    '''
    
    if channel_table != queries.vbrp:
        if not os.path.exists(variable.location+"\\"+filenm[0]):
            return 'File not found'
        df = process_data.get_data(filenm)
        procedure.starting(conx, channel_table, 'truncate')
    else:
        procedure.starting(conx, channel_table, 'truncate')
        df = get_vbrp()
    if channel_table != queries.vbrp:
        if channel_table['num'] != False:
            for i in channel_table['num']:
                df[i] = df[i].str.replace(",", '')
        df[channel_table['dates']] = df[channel_table['dates']].apply(pd.to_datetime, errors='coerce', format="%d-%m-%Y")
    else:
        for i in channel_table['num']:
             df[i] = pd.to_numeric(df[i])
        df[channel_table['dates']] = df[channel_table['dates']].apply(pd.to_datetime, errors='coerce', format="%Y%m%d")
        for i in range(len(df['Time'])):
            vl = df.at[i, 'Time']
            vl = vl[:2] + ':' + vl[2:4] + ':' + vl[4:]
            df.at[i, 'Time'] = vl
    df.fillna('', inplace=True)
    if channel_table == queries.vbrp:
        df['Payer'] = df['Payer'].str.replace('^0+', '', regex=True)
        df['Sold-To Pt'] = df['Sold-To Pt'].str.replace('^0+', '', regex=True)
        df['Material'] = df['Material'].str.replace('^0+', '', regex=True)
        df['Bill.Doc.'] = df['Bill.Doc.'].str.replace('^0+', '', regex=True)
    elif channel_table == queries.zfbl5n:
        df['Account'] = df['Account'].str.replace('^0+', '', regex=True)
        df['Assignment'] = df['Assignment'].str.replace('^0+', '', regex=True)
    df = df.values.tolist()
    df = procedure.fill_null(df)
    df = procedure.fill_NaT(df)
    process_data.sql_insert(df, channel_table['insert'], cursor=conx.cursor())

con = sql_con.get_con("Sales_Source_Files")
insert_into(con, queries.vbrp, variable.vbrp)
insert_into(con, queries.zfbl5n, variable.zfbl5n)
insert_into(con, queries.inv_odn, variable.inv_odn)

os.system(f'''cmd /c sqlcmd -Q " [Finance].[dbo].[VBRP_proc] '2024-08-01' " -o "D:\SAP_files\Logs\Validation\vbrp_proc.csv" -s "," ''')

con.close()

print("--- %s seconds ---" % (time.time() - start_time))