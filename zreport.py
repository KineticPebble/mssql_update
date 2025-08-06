
import time
start_time = time.time()
import sql_con
import queries
import variable
import os
import process_data
import procedure
import pandas as pd



def zrepot(conx: object, channel_table: dict, filenm: list, query: str) -> None:
    '''Update zmakt data

    Parameters:
        conx: Database object
        channel_table: channel and table details
        filenm: list containing filenames

    Returns:
        None
    '''
    
    if not os.path.exists(variable.location+"\\"+filenm[0]):
        return 'File not found'
    
    procedure.starting(conx, channel_table, 'truncate')
    df = process_data.get_data(filenm)
    for i in channel_table['num']:
        df[i] = df[i].str.replace(",", '')
    for i in channel_table['cl']:
        df[i] = df[i].str.slice(0,255)
    df[channel_table['dates']] = df[channel_table['dates']].apply(pd.to_datetime, errors='coerce', format="%d-%m-%Y")
    df.fillna('', inplace=True)
    df = df.values.tolist()
    df = procedure.fill_null(df)
    df = procedure.fill_NaT(df)
    process_data.sql_insert(df, query, cursor=conx.cursor())

con = sql_con.get_con("SSF")
zrepot(con, queries.zmakt_table, variable.zmakt, queries.zmakt_insert)
zrepot(con, queries.zomni_table, variable.zomni, queries.zomni_insert)
con.close()

print("--- %s seconds ---" % (time.time() - start_time))