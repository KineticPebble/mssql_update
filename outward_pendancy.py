'''File containing function for udpating Gatein, Gateout, Gatehold_invoice, Gatehold_delivery

1 function:
    - gateinout
'''
import process_data
import procedure
import pandas as pd
import os
import variable

def gateinout(conx: object, channel_table: dict, filenm: list) -> None:
    '''function for udpating Gatein, Gateout, Gatehold_invoice, Gatehold_delivery

    Parameters:
        conx: database connection object
        channel_table: dict contaning table data details
        filenm: List containing filenames

    Returns:
        None
    '''
    if not os.path.exists(variable.location+"\\"+filenm[0]):
        return 'File not found'
    print(f"------{channel_table['name']}------")
    procedure.run_delete_data(channel_table['delete'], cursor = conx.cursor())
    df = process_data.get_data(filenm)
    if channel_table['add'] != False:
        for c in channel_table['add']:
            df.insert(len(df.columns), c, None)
    if channel_table['columns'] != False:
        df = df[channel_table['columns']]
    if channel_table['dates'] != False:
        df[channel_table['dates']] = df[channel_table['dates']].apply(pd.to_datetime, errors='coerce', format="%d-%m-%Y")
        df = df.values.tolist()
        df = procedure.fill_NaT(df)
    else: df = df.values.tolist()
    print("inserting")
    process_data.sql_insert(df, channel_table['insert'], cursor=conx.cursor())


    
    

