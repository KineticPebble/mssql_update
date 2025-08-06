import time
start_time = time.time()
'''ZPO data update

1 function:
    - zpo
'''
import sql_con
import queries
import process_data
import procedure
import os
import variable
import teams_msg
import logging

def log(flnm: str) -> logging.basicConfig:
    ''' Log function for logging

    Parameters:
        flnm: Filename

    Returns:
        logging object which is used to write logs to file
    '''
    fullname = variable.log_loc+"\\"+"Logs\\"+flnm+".log"
    logging.basicConfig(level=logging.INFO, filename=fullname, filemode='w', format='%(asctime)s -- %(levelname)s -- %(message)s')
    return logging

current_file = 'ZPO'

logging = log(current_file)

def send_log(subject: str) -> None:
    '''Send message on Teams channel

    Parameters:
    subject: subject of the message
    '''
    logging.exception("ERROR")
    time.sleep(2)
    teams_msg.msg_teams(teams_msg.log_html(r"D:\SAP_files\Logs"+"\\"+current_file+".log"), subject=subject)


def zpo(conx: object, channel_table: dict, filenm: list) -> None:
    '''Update zpo data

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
    df.drop(["ZBS_SEASON"], axis=1, inplace=True)
    df['Vendor Code'] = df['Vendor Code'].str.replace("^0+", '', regex=True)
    num_cl = ['PO Qty', 'Cumulative GR Qty', 'Balance GR Qty', 'PO Net Price', 'PO MRP', 'PO MRP Val', 'PO GRN Val', 'PO Bal Val', 'PO Net Price in INR', 'PO Cost Val', 'PO Miro Cost Val', 'Article MRP', 'Discount Amount', 'Discount Amount-RA06 INR']
    for i in num_cl:
        df[i] = df[i].str.replace(",", '')
    df.loc[~df['Actual In DC Date'].str.match("^\d\d\.\d\d\.\d\d\d\d"), 'Actual In DC Date'] = ''
    df.fillna('', inplace=True)
    df = df.values.tolist()
    df = procedure.fill_null(df)
    process_data.sql_insert(df, queries.zpo_insert, cursor=conx.cursor())

try:
    logging.info("ZPO")
    result = zpo(sql_con.get_con("Vendor"), queries.zpo_tables, variable.zpo_files)
    if result is not None:
        logging.info(result)
        teams_msg.msg_teams(teams_msg.log_html(r"D:\SAP_files\Logs"+"\\"+current_file+".log"), subject="Error")
except:
    send_log("ZPO file update error")
    exit()

logging.info("running SP")
print("running SP")
os.system(f'''cmd /c sqlcmd -Q " {queries.zpo_tables['SP']} "  -o "D:\SAP_files\Logs\Validation\zpo.csv" -s "," ''')
os.system('''cmd /c sqlcmd -Q " EXEC [INVT_W].[dbo].[Week_To_Date_SellThru_Update] "  -o "D:\SAP_files\Logs\Validation\Sellthru.csv" -s "," ''')
os.system(f'''cmd /c sqlcmd -Q " EXEC [FACT].dbo.[Weekly_Option_Sales_Catseason_SP] '2024-08-01', '{variable.lmd}' "  -o "D:\SAP_files\Logs\Validation\Weekly_cat_season.csv" -s "," ''')
os.system('''cmd /c sqlcmd -Q " exec [FACT].dbo.Channel_Article_Sales_SP "  -o "D:\SAP_files\Logs\Validation\Channel_article_sales.csv" -s "," ''')
print("--- %s seconds ---" % (time.time() - start_time))

logging.info("Completed")
teams_msg.msg_teams(teams_msg.log_html(r"D:\SAP_files\Logs"+"\\"+current_file+".log"), subject="Load Completed")
