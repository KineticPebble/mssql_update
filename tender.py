'''Tender data update

1 function:
    - tender
'''

import queries
import process_data
import procedure
import os
import variable

def tender(conx: object, channel_table: dict, filenm: list) -> None:
    '''Update Tender data

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
    df.drop(columns=df.columns[-2:],  axis=1,  inplace=True)
    df = df.values.tolist()
    df = procedure.fill_null(df)
    process_data.sql_insert(df, queries.tender_insert, cursor=conx.cursor())
    
