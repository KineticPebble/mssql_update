'''file for updating tables in SSIS_Upload

3 functions:
    - omni
    - outward2
    - zsis
'''

import queries
import process_data
import procedure
import os
import variable
import pandas as pd

def omni(conx: object, channel_table: dict, filenm: list) -> None:
    '''Omni channels data update

    Parameters:
        conx: Database connection object
        channel_table: dict contaning table data details
        filenm: List containing filenames

    Returns:
        None
    '''
    if not os.path.exists(variable.location+"\\"+filenm[0]):
        return 'File not found'
    procedure.starting(conx, channel_table)
    print("Processing Files")
    df = process_data.get_data(filenm)
    df['Forward Address'] =  df['Forward Address'].str.replace("\t", '')
    df['Pickup Address'] =  df['Pickup Address'].str.replace("\t", '')
    df = df.values.tolist()
    df = procedure.fill_null(df)
    print("inserting")
    process_data.sql_insert(df, queries.Omni_insert, cursor=conx.cursor())
    print(f"Deleting {channel_table['final']}")
    procedure.delete_data(channel_table['final'], cursor=conx.cursor())
    procedure.final(conx, channel_table)
    procedure.run_SP(channel_table['SP'], cursor=conx.cursor())

def outward2(conx: object, channel_table:dict, filenm: list, data_type:str=False) -> None:
    '''function for updating outward2 sap files.
    Each channel have their own requirements.

    Parameters:
        conx: Database connection object
        channel_table: dict contaning table data details
        filenm: List containing filenames
        data_type: for changing behavior according to file and table requirement

    Returns:
        None
    '''
    if not os.path.exists(variable.location+"\\"+filenm[0]):
        return 'File not found'
    if data_type == 'Online-18': procedure.run_delete_data(channel_table['delete'], cursor=conx.cursor())
    else: procedure.starting(conx, channel_table)
    print("Processing Files")
    df = process_data.get_data(filenm)
    if data_type == False:
        df.drop(columns=df.columns[-7:],  axis=1,  inplace=True)
        df = df.values.tolist()
        df = procedure.fill_null(df)
        print("inserting")
        process_data.sql_insert(df, queries.outward_insert(channel_table['delete']), cursor=conx.cursor())
    elif data_type == 'Outright':
        for c in channel_table['add']:
            df.insert(len(df.columns), c, None)
        df = df[channel_table['columns']]
        df = df.values.tolist()
        print("inserting")
        process_data.sql_insert(df, queries.outright_insert, cursor=conx.cursor())
    elif data_type == 'Online-18':
        for c in channel_table['add']:
            df.insert(len(df.columns), c, None)
        df = df[channel_table['columns']]
        df[channel_table['dates']] = df[channel_table['dates']].apply(pd.to_datetime, errors='coerce', format="%d-%m-%Y")
        df = df.values.tolist()
        df = procedure.fill_NaT(df)
        print("inserting")
        process_data.sql_insert(df, queries.online_18_insert, cursor=conx.cursor())
    if 'final' in channel_table.keys():
        print(f"Deleting :{channel_table['final']}")
        procedure.delete_data(channel_table['final'], cursor=conx.cursor())
        procedure.final(conx, channel_table)
    procedure.run_SP(channel_table['SP'], cursor=conx.cursor())

def zsis(conx: object, channel_table: dict, filenm: list) -> None:
    '''Update zsis

    Parameters:
        conx: Database connection object
        channel_table: dict contaning table data details
        filenm: List containing filenames

    Returns:
        None
    '''
    if not os.path.exists(variable.location+"\\"+filenm[0]):
        return 'File not found'
    procedure.starting(conx, channel_table, command='truncate')
    df = process_data.get_data(filenm)
    df.insert(0, 'col1', None)
    df = df.values.tolist()
    print("inserting")
    process_data.sql_insert(df, queries.zsis_insert, cursor=conx.cursor())
    procedure.run_SP(channel_table['SP'], cursor=conx.cursor())
    




    
