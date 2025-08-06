'''File containing repeated procedures

7 functions:
Delete_data
run_delete_data
fill_null
fill_NaT
starting
final
run_sap
'''
import pandas as pd

def delete_data(table: str, cursor: object, command:str=False) -> None:
    '''Delates or truncates the data from the table

    Parameters:
        table: Table name
        cursor: Databse cursor object
        command: False is delete. truncate is truncate process

    Retunrs:
        None
    '''
    if command == 'truncate': sqlq = f'''truncate table {table};'''
    else: sqlq = f'''Delete from {table};'''
    cursor.execute(sqlq)
    cursor.commit()
    cursor.close()

def run_delete_data(q:str, cursor: object) -> None:
    '''Just for running query directly

    Parameters:
        q: Query text
        cursor: Database cursor object

    Returns:
        None

    '''
    cursor.execute(q)
    cursor.commit()
    cursor.close()

def fill_null(df: list) -> list:
    '''coneverts empty string to None from the data

    Parameters:
        df: 2 dimentional list containing tabular data

    Returns:
        modified list
    '''
    print("filling NULL")
    for l in range(len(df)):
        df[l] = [x if x != '' else None for x in df[l]]
    return df

def fill_NaT(df: list) -> list:
    '''converts NaT datatype to None from the data

    Parameters:
        df: 2 dimentional list containing tabular data

    Returns:
        modified list
    '''
    print("filling_NaT")
    for l in range(len(df)):
        df[l] = [x if type(x) != pd._libs.tslibs.nattype.NaTType else None for x in df[l]]
    return df

def starting(conx: object, channel_table: dict, command:str=False) -> None:
    '''prints table name and deletes the table data

    Parameters:
        conx: Database connection object
        channel_table: Dict contaning channel table and data details
        command: False is delete. truncate is truncate process

    Returns:
        None
    '''
    print(f"------{channel_table['delete']}------")
    print(f"Deleting {channel_table['delete']}")
    delete_data(channel_table['delete'], cursor=conx.cursor(), command=command)

def final(conx: object, channel_table: dict) -> None:
    '''clean data with insert query

    Parameters:
        conx: Database connection object
        channel_table: Dict contaning channel table and data details

    Returns:
        None
    '''
    print("final Insert")
    cursor=conx.cursor()
    cursor.execute(channel_table['insert'])
    cursor.commit()
    cursor.close()

def run_SP(q: str, cursor: object) -> None:
    '''For running any query directly

    Parameters:
        q: Query text
        cursor: Database cursor object
    
    Returns:
        None
    '''
    print("Running ", q)
    cursor.execute(q)
    cursor.commit()
    cursor.close()
