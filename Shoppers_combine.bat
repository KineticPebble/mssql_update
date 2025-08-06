cd /d D:\Scripts\mssql_update
taskkill /F /T /FI "USERNAME eq %USERNAME%" /IM excel.exe
D:\Scripts\sql_update\Scripts\python.exe combine_files.py