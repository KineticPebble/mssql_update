'''This is the main file for ETL_process which uses all the function defined in varoius script for various channel tables.
Most of the things are wrapped in try except to prevent the script from stopping. The error message will be recorded in log and the log will be immediatly sent.
sqlcmd is used to run Stored Procedure from sql server
There are few functions which could be kept in other scripts

2 functions:
    - log
    - send_log

'''

import time
start_time = time.time()
import pyodbc
import auth
import SSIS_upload_update
import queries
import variable
import tender
import outward_pendancy
import logging
import teams_msg
import os
from validation_fix import fix
import dc_stock
import VBRP
import sql_con

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

current_file = 'ETL'
logging = log(current_file)

def send_log(subject: str) -> None:
    '''Send message on Teams channel

    Parameters:
    subject: subject of the message
    '''
    logging.exception("ERROR")
    time.sleep(2)
    teams_msg.msg_teams(teams_msg.log_html(r"D:\SAP_files\Logs"+"\\"+current_file+".log"), subject=subject)

try:
    logging.info("Connecting Database")
    database = "SSIS_upload"
    connect_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.91.7.46;'
    connect_string += f'DATABASE={database};UID={auth.usr};PWD={auth.ps}'
    connection = pyodbc.connect(connect_string)
except:
    send_log("Database connection error")

try:
    logging.info("ZSIS")
    result = SSIS_upload_update.zsis(connection, queries.zsis, variable.zsis)
    if result is not None: logging.info(result)
except: send_log("ZSIS file update error")
try:
    logging.info("Omni")
    result = SSIS_upload_update.omni(connection, queries.omni_tables, variable.omni_files)
    if result is not None: logging.info(result)
except: send_log("Omni file update error")
try:
    logging.info("scrap")
    result = SSIS_upload_update.outward2(connection, queries.scrap_tables, variable.scrap)
    if result is not None: logging.info(result)
except: send_log("Scrap file update error")
try:
    logging.info("produkt")
    result = SSIS_upload_update.outward2(connection, queries.produkt_table, variable.produkt)
    if result is not None: logging.info(result)
except: send_log("produkt file update error")
try:
    logging.info("export")
    result = SSIS_upload_update.outward2(connection, queries.export_table, variable.export)
    if result is not None: logging.info(result)
except: send_log("export file update error")
try:
    logging.info("outright")
    result = SSIS_upload_update.outward2(connection, queries.outright_table, variable.outright, 'Outright')
    if result is not None: logging.info(result)
except: send_log("outright file update error")
try: 
    logging.info("Online-18")
    result = SSIS_upload_update.outward2(connection, queries.online_18_table, variable.online_or, 'Online-18')
    if result is not None: logging.info(result)
except: send_log("Online-18 file update error")
try: 
    logging.info("Tender")
    result = tender.tender(connection, queries.tender, variable.tender_files)
    if result is not None: logging.info(result)
    logging.info("Tender_SP")
    os.system('''cmd /c sqlcmd -i "D:\Scripts\mssql_update\Tender_SP.sql" ''')
except: send_log("Tender file update error")
try: 
    logging.info("DC Stock")
    result = dc_stock.stock_dc(connection, queries.dc_stock, variable.dc_stock)
    if result is not None: logging.info(result)
    os.system(f'''cmd /c sqlcmd -Q " {queries.dc_stock_SP} " -o "D:\SAP_files\Logs\Validation\DC stock.csv" -s "," ''')
except: send_log("DC Stock update error")
try:
    logging.info("Gatein")
    result = outward_pendancy.gateinout(connection, queries.gatein, variable.gatein)
    if result is not None: logging.info(result)
except: send_log("Gatein file update error")
try:
    logging.info("Gateout")
    result = outward_pendancy.gateinout(connection, queries.gateout, variable.gateout)
    if result is not None: logging.info(result)
except: send_log("Gateout file update error")
try:
    logging.info("Gatehold_Invoice")
    result = outward_pendancy.gateinout(connection, queries.gatehold_invoice, variable.gatehold_invoice_files)
    if result is not None: logging.info(result)
except: send_log("Gatehold_Invoice file update error")
try:
    logging.info("Gatehold_Delivery")
    result = outward_pendancy.gateinout(connection, queries.gatehold_delivery, variable.gatehold_delivery)
    if result is not None: logging.info(result)
except: send_log("Gatehold_Delivery file update error")        

connection.close()

try:
    logging.info("Outward_pendency")
    os.system(f'''cmd /c sqlcmd -Q " {queries.outward_pendency_SP} " -o "D:\SAP_files\Logs\Validation\Outward_pendency.csv" -s "," ''')
except: send_log("Outward_pendency SP error")
try:
    logging.info("Stock_OH")
    os.system(f'''cmd /c sqlcmd -Q " {queries.stock_OH} " -o "D:\SAP_files\Logs\Validation\Stock_OH.csv" -s "," ''')
except: send_log("Stock_OH SP error")
try:
    logging.info("Insert_V2")
    os.system(f'''cmd /c sqlcmd -Q " {queries.insert_V2} " ''')
except: send_log("Insert_V2 SP Error")
try:
    logging.info("D2")
    os.system(f'''cmd /c sqlcmd -Q " {queries.D2} " ''')
    os.system('''cmd /c sqlcmd -Q "exec [FACT].[dbo].[D2 Validation] @FromDate = '2022-08-01'" -o "D:\SAP_files\Logs\Validation\D2.csv" -s "," ''')
    os.system('''cmd /c findstr /v /c:"----" "D:\SAP_files\Logs\Validation\D2.csv" > "D:\SAP_files\Logs\Validation\D2 Validation.csv" ''')
    fix(r"D:\SAP_files\Logs\Validation\D2 Validation.csv", r"D:\SAP_files\Logs\Validation\D2_Validation.csv")
except: send_log("D2 SP Error")
try:
    logging.info("Main_Insert")
    os.system(f'''cmd /c sqlcmd -Q " {queries.main_insert} " ''')
    os.system('''cmd /c sqlcmd -Q "exec [INVT_W].[dbo].[Insert Validation]" -o "D:\SAP_files\Logs\Validation\Insert.csv" -s "," ''')
    os.system('''cmd /c findstr /v /c:"----" "D:\SAP_files\Logs\Validation\Insert.csv" > "D:\SAP_files\Logs\Validation\Insert Validation.csv" ''')
    fix(r"D:\SAP_files\Logs\Validation\Insert Validation.csv", r"D:\SAP_files\Logs\Validation\Insert_Validation.csv")
except: send_log("main_insert SP Error")
try:
    logging.info("Bucket")
    os.system(f'''cmd /c sqlcmd -Q " {queries.bucket} " -o "D:\SAP_files\Logs\Validation\Bucket.csv" -s "," ''')
except: send_log("Bucket SP Error")
try:
    logging.info("D3")
    os.system(f'''cmd /c sqlcmd -Q " {queries.D3} " -o "D:\SAP_files\Logs\Validation\D3.csv" -s "," ''')
except: send_log("D3 SP Error")
try:
    logging.info("D4")
    os.system(f'''cmd /c sqlcmd -Q " {queries.D4} " -o "D:\SAP_files\Logs\Validation\D4.csv" -s "," ''')
except: send_log("D4 SP Error")
try:
    logging.info("D5")
    os.system(f'''cmd /c sqlcmd -Q " {queries.D5} " -o "D:\SAP_files\Logs\Validation\D5.csv" -s "," ''')
except: send_log("D5 SP Error")
try:
    logging.info("D6")
    os.system(f'''cmd /c sqlcmd -Q " {queries.D6} " -o "D:\SAP_files\Logs\Validation\D6.csv" -s "," ''')
except: send_log("D6 SP Error")
try:
    logging.info("LastWeek")
    os.system(f'''cmd /c sqlcmd -Q " {queries.lastweek} " -o "D:\SAP_files\Logs\Validation\Lastweek.csv" -s "," ''')
except: send_log("LastWeek SP Error")
try:
    logging.info("LastWeek_V2")
    os.system(f'''cmd /c sqlcmd -Q " {queries.lastweek_V2} " -o "D:\SAP_files\Logs\Validation\Lastweek_V2.csv" -s "," ''')
except: send_log("LastWeek_V2 SP Error")
try:
    logging.info("FC_DAILY_SALES")
    os.system(f'''cmd /c sqlcmd -Q " {queries.fc_daily_sales} " -o "D:\SAP_files\Logs\Validation\FC_DAILY_SALES.csv" -s "," ''')
except: send_log("FC_DAILY_SALES Error")
try:
    logging.info("ONOOS_Stock")
    os.system(f'''cmd /c sqlcmd -Q " {queries.onoos_stock} " -o "D:\SAP_files\Logs\Validation\ONOOS_stock.csv" -s "," ''')
except: send_log("ONNOS Error")


print("--- %s seconds ---" % (time.time() - start_time))
logging.info("Completed")
teams_msg.msg_teams(teams_msg.log_html(r"D:\SAP_files\Logs"+"\\"+current_file+".log"), subject="Load Completed")

try:
    logging.info("VBRP")
    con = sql_con.get_con("Sales_Source_Files")
    VBRP.insert_into(con, queries.vbrp, variable.vbrp)
    VBRP.insert_into(con, queries.zfbl5n, variable.zfbl5n)
    VBRP.insert_into(con, queries.inv_odn, variable.inv_odn)
    con.close()
    logging.info("running SP")
    os.system(f'''cmd /c sqlcmd -Q " [Finance].[dbo].[VBRP_proc] '2024-08-01' " -o "D:\SAP_files\Logs\Validation\\vbrp_proc.csv" -s "," ''')
except:
    send_log("VBRP Error")

try:
    logging.info("WB")
    os.system(f'''cmd /c sqlcmd -Q " {queries.WB13} " -o "D:\SAP_files\Logs\Validation\WB13.csv" -s "," ''')
    os.system(f'''cmd /c sqlcmd -Q " {queries.WB14} " -o "D:\SAP_files\Logs\Validation\WB14.csv" -s "," ''')
    os.system(f'''cmd /c sqlcmd -Q " {queries.WB15} " -o "D:\SAP_files\Logs\Validation\WB15.csv" -s "," ''')
    os.system(f'''cmd /c sqlcmd -Q " {queries.WB16} " -o "D:\SAP_files\Logs\Validation\WB16.csv" -s "," ''')
    os.system(f'''cmd /c sqlcmd -Q " {queries.WB17} " -o "D:\SAP_files\Logs\Validation\WB17.csv" -s "," ''')
    os.system(f'''cmd /c sqlcmd -Q " {queries.WB18} " -o "D:\SAP_files\Logs\Validation\WB18.csv" -s "," ''')
except: send_log("WB Error")

