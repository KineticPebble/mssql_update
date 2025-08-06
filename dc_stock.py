'''This file contains one function called stock_dc which take connection object,
channel properties and file list and updates the table with the data.

'''

import queries
import process_data
import procedure
import os
import variable
import pandas as pd

def stock_dc(conx: object, channel_table: dict, filenm: list) -> None:
    '''Update the DC stock files

    Parameters:
        conx: sql connection object
        channel_table: Dict containing properties of the channel
        filenm: list of filenames

    Returns:
        None
    '''
    if not os.path.exists(variable.location+"\\"+filenm[0]):
        return 'File not found'
    procedure.starting(conx, channel_table, 'truncate')
    print("Processing Files")
    df = process_data.get_data(filenm)
    df.drop(df[df['Quantity'].str.contains("-")].index, inplace=True)
    df = df.values.tolist()
    df = procedure.fill_null(df)
    process_data.sql_insert(df, queries.dc_stock_insert, cursor=conx.cursor())
    
