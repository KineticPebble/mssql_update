cd /d D:\Scripts\mssql_update
taskkill /F /T /FI "USERNAME eq %USERNAME%" /IM excel.exe
taskkill /F /T /FI "USERNAME eq %USERNAME%" /IM python.exe
taskkill /F /T /FI "USERNAME eq %USERNAME%" /im saplogon.exe
D:\Scripts\sql_update\Scripts\python.exe main.py