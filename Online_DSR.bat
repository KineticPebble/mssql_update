del /Q "D:\Files\Input\Online DSR\*"
copy /Y "\\BOT\Robotics_Automation\Performance Reporting\FMDSR\Month_2025\FinalDSR.xlsb" "D:\Files\Input\Online DSR\Online DSR.xlsb"
cd /d D:\Scripts\mssql_update
D:\Scripts\sql_update\Scripts\python.exee Online_DSR.py
