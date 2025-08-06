This is the codebase which was maily used for pusing data to MSSQL server.
There are many python scripts other than main one which process and push other kinds of data and insert into MSSQL server.
There are many python scripts which are imported including some standard library and some from pypi repository. most of them are also used in other scripts in this codebase.
Most of the scripts are executed via bat script.


# ETL Process – Main Controller Script, ETL.bat(main.py)

## Overview

This ETL (Extract, Transform, Load) project automates the data extraction from SAP-related Excel and text files, transforms the data according to business rules, and loads it into a SQL Server database using stored procedures and custom Python logic. It supports multiple channels such as ZSIS, Omni, Tender, Scrap, Outright, Gatehold, VBRP, and others.  

Logging and notifications are handled via Python's logging module and Microsoft Teams webhooks.

---

## 📁 Project Structure

```bash
.
├── main.py                  # Main ETL runner script
├── SSIS_upload_update.py    # Handles SSIS upload updates for Omni, ZSIS, Scrap, etc.
├── outward_pendancy.py      # Gate-in/Out/Hold file processor
├── tender.py                # Handles tender file updates
├── VBRP.py                  # Special handler for VBRP, ZFBL5N, and invoice ODN
├── process_data.py          # Converts Excel to CSV and extracts pandas DataFrames
├── procedure.py             # SQL delete/insert utility functions
├── teams_msg.py             # Sends logs and errors to MS Teams
├── variable.py              # Centralized configuration (filenames, paths, dates)
├── querries.py              # SQL queries and other supporting data
├── auth                     # Contains the credential required for authentication
├── logging                  # Script for logging execution
├── validation_fix           # Fixes the 
├── dc_stock                 # Distribution center processor
├── sql_con                  # sql connector funcion

```

---

## 🚀 How It Works

### 1. **Startup and Logging**
- `main.py` initializes logging using the `log()` function.
- Errors are caught using `try-except` blocks.
- Errors are logged and sent to a Teams channel using `send_log()`.

### 2. **Database Connection**
```python
pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=...;DATABASE=...;UID=...;PWD=...")
```

---

## 🧱 ETL Modules

### ✅ SSIS Upload Updates (`SSIS_upload_update.py`)
Processes data for:
- **ZSIS**: Truncates the table, inserts CSV with one extra column.
- **Omni**: Adds forward/pickup address processing, deletes and reloads data.
- **Outward2**: Handles multiple types (`Online-18`, `Outright`, others) with custom transformation logic.

### ✅ Gatehold and Delivery (`outward_pendancy.py`)
Processes:
- Gatein
- Gateout
- Gatehold Invoice
- Gatehold Delivery

### ✅ Tender Upload (`tender.py`)
- Drops last two columns before insert.
- Uses `truncate` to clean table before insert.

### ✅ VBRP Upload (`VBRP.py`)
- Pulls data via HANA connector (`hdbcli`) or Excel files.
- Supports VBRP, ZFBL5N, and Invoice Mapping (ODN).
- Performs type casting, date formatting, zero-stripping, and inserts.

### ✅ DC stock (`dc_stock.py`)
- Pulls data from txt files.
- performs required transformation database insertion.

---

## 🧪 Data Processing & Utility Modules

### 🛠 process_data.py
- `covert_to_csv()`: Converts XLSX to CSV using Excel COM.
- `get_data()`: Reads and transforms files into DataFrames.
- `sql_insert()`: Bulk inserts with `executemany`.

### 🛠 procedure.py
- Functions for:
  - `delete_data()`, `starting()`, `final()`, `fill_null()`, `fill_NaT()`
  - Executes stored procedures or SQL deletes/truncates.

---

## 🔔 Notifications

### teams_msg.py
- Uses Microsoft Teams connector via `pymsteams`.
- Converts logs to HTML and sends them as messages.

---

## ⚙️ Configuration

### variable.py
Contains:
- File lists: `omni_files`, `tender_files`, `gatein`, `zsis`, etc.
- Date variables: `ETL_rundate`, `MTD_15`, `Online_18_rundate`, etc.
- File paths: `location`, `log_loc`, etc.

---

## 📝 Logging & Validation

- All logs are stored in: `D:\SAP_files\Logs\{script_name}.log`
- Output CSVs from stored procedures are saved in `D:\SAP_files\Logs\Validation\`

---

## ✅ Execution Flow (main.py)

1. Connect to DB.
2. Process:
   - ZSIS
   - Omni
   - Scrap
   - Produkt
   - Export
   - Outright
   - Online-18
   - Tender
   - DC Stock
   - Gatein/Gateout
   - Gatehold (Invoice & Delivery)
3. Execute Stored Procedures
4. Run VBRP pipeline
5. Execute various validations: D2, D3 etc.
6. Send completion message via Teams.

---

## 🛡️ Error Handling

Each block in `main.py` is wrapped in a `try-except`. On exception:
- Logs are written
- A Teams notification is sent
- The script continues with the next step

---

## 🔧 Requirements

- Python 3.x
- `pyodbc`
- `pandas`
- `pymsteams`
- `win32com.client` (Windows only)
- `hdbcli` (SAP HANA)

---

## 📬 Final Message

Once execution completes, `main.py` sends a final success message and log content to Microsoft Teams.

---

# bcbr_main.bat(bcbr_dump.py), bcbrpf.bat(bcbrpf.py)

#### Purpose:
The scripts `bcbr_dump.py` and `bcbrpf.py` are designed to handle the download, processing, and upload of specific CSV files to a SQL database. They use SFTP for file transfer and perform necessary data transformations before inserting the data into target tables.

#### Main Components:

1. **Imports:**
   - Imports necessary modules (`time`, `pandas`, `sql_con`, `datetime`, `os`, `glob`, `procedure`, `sftpop`, `variable`).

2. **Global Variables:**
   - Defines download locations, source directories, dates, and SQL stored procedures using variables from other modules (`variable.tddmy_`, `variable.tdmdy`).

3. **File Transfer Functions:**
   - Connects to an SFTP server using `sftpop.sftp.connect`.
   - Downloads the latest CSV file based on a date pattern.
   - Deletes existing files in the download location.

4. **Data Processing and Upload:**

   - **bcbr_dump.py:**
     - Reads data from the downloaded CSV file into a pandas DataFrame.
     - Handles specific columns and data types for BCBR data.
     - Inserts data into the `[PROD].[dbo].[Main_BCBR_SSIS]` table using SQL commands.

   - **bcbrpf.py:**
     - Reads data from the downloaded CSV file into a pandas DataFrame.
     - Handles specific columns and data types for PF (Pick Failure) data.
     - Inserts data into the `[PROD].[dbo].[PF_Temp]` table using SQL commands.

5. **Database Operations:**
   - Establishes a connection to the target database (`PROD`) using `sql_con.get_con`.
   - Deletes existing data from the target tables before inserting new data.
   - Uses `procedure.fill_null` and `procedure.fill_NaT` for null value handling.
   - Executes batch inserts in chunks of 25,000 rows.

6. **Stored Procedure Execution:**
   - Runs stored procedures after loading data to perform additional processing or updates.
   - Logs the output of the stored procedures to a CSV file.

7. **Logging and Cleanup:**
   - Logs important steps and completion times.
   - Closes the database connection after processing.

---
# Journey.bat(break_point.py), RJ.bat (Receipt_journey.py)

#### Purpose:
The scripts `break_point.py` and `Receipt_journey.py` are designed to handle the download, processing, and upload of specific CSV files to a SQL database. They use SFTP for file transfer and perform necessary data transformations before inserting the data into target tables.

#### Main Components:

1. **Imports:**
   - Imports necessary modules (`time`, `paramiko.ecdsakey`, `pandas`, `sql_con`, `datetime`, `procedure`, `sftpop`, `variable`, `glob`, `os`, `pysftp`).

2. **Global Variables:**
   - Defines download locations, source directories, dates, and SQL stored procedures using variables from other modules (`variable.ytdmy_`, `variable.tdymd`).

3. **File Transfer Functions:**

   - **break_point.py:**
     - Connects to an SFTP server using `pysftp`.
     - Deletes existing files in the download location.
     - Defines functions to get and download the latest CSV file based on a date pattern.

   - **Receipt_journey.py:**
     - Similar to `break_point.py`, but with different file patterns and additional handling for historical data and receipts.

4. **Data Processing and Upload:**

   - **break_point.py:**
     - Reads data from the downloaded CSV files into pandas DataFrames.
     - Handles specific columns and data types for various data types (JBP, JWAT, LUU).
     - Inserts data into target tables (`JBP`, `JWAT`, `LUU`) using SQL commands.

   - **Receipt_journey.py:**
     - Reads data from the downloaded CSV files into pandas DataFrames.
     - Handles specific columns and data types for Receipts.
     - Inserts data into the `[COFP].dbo.[Receipt]` table using SQL commands.

5. **Database Operations:**
   - Establishes a connection to the target database (`COFP`) using `sql_con.get_con`.
   - Deletes existing data from target tables before inserting new data.
   - Uses `procedure.fill_null` and `procedure.fill_NaT` for null value handling.
   - Executes batch inserts in chunks of 25,000 rows.

6. **Stored Procedure Execution:**
   - Runs stored procedures after loading data to perform additional processing or updates.
   - Logs the output of the stored procedures to a CSV file.

7. **Logging and Cleanup:**
   - Logs important steps and completion times.
   - Closes the database connection after processing.
---
# GCP_upload.bat(GCP_upload.py)

#### Purpose:
The script `GCP_upload.py` is designed to track changes in data from a SQL database and upload specific files based on those changes to Google Cloud Storage (GCS). It handles different types of data (Sales, Targets, Stock) for various channels and performs necessary file conversions before uploading.

#### Main Components:

1. **Imports:**
   - Imports necessary modules (`sql_con`, `variable`, `logging`, `GCP_queries`, `pandas`, `datetime`, `dateutil.relativedelta`, `random`).

2. **Global Variables:**
   - Defines the location for GCP logs using a variable from another module (`variable.GCP_log_loc`).
   - Specifies the current date using a variable defined in another module (`variable.tddmy_`).

3. **Logging Configuration:**
   - Sets up logging to write messages to a log file with timestamps.

4. **Data Fetching and Normalization:**
   - Connects to the SQL database using `sql_con.get_con`.
   - Calls `GCP_queries.data_tracker` to fetch old and new data.
   - Normalizes the fetched data into pandas DataFrames for easier manipulation.

5. **Change Calculation:**
   - Calculates differences between old and new data for various metrics (Sales, Target ABP, Target Field, Target Margin, Stock).

6. **Identifying Changes:**
   - Identifies significant changes in Sales, Target ABP, Target Field, Target Margin, and Stock.
   - Determines the type of data file to upload based on the channel.

7. **File Conversion and Upload:**
   - Defines a function `changes` to determine which files need to be uploaded based on data changes.
   - Defines a function `ETL` (Extract, Transform, Load) to:
     - Query data from the database based on date ranges.
     - Save the query results as a CSV file.
     - Convert the CSV file to `.xlsb` format if necessary.
     - Upload the converted file to GCS.

8. **Logging and Execution:**
   - Logs the data to be uploaded for each channel.
   - Iterates through the list of files to upload and calls `ETL` for each entry.
   - Closes the database connection after processing.

---
# captive_upload.bat(captive_upload.py)

### Documentation of `captive_upload.py`

#### Purpose:
The script `captive_upload.py` is designed to fetch data from a SQL database, convert it into a CSV file, and then upload the CSV file to Google Cloud Storage (GCS). The process involves fetching data based on a date range, converting it to a different format if necessary, and uploading it to GCS for further processing.

#### Main Components:

1. **Imports:**
   - Imports necessary modules (`auth`, `pyodbc`, `csv`, `win32com.client`, `variable`, `storage` from `google.cloud`).

2. **Global Variables:**
   - Defines the database connection string and SQL query for fetching data.
   - Specifies the date range (`from_date`) using a variable defined in another module (`variable.lmfd`).

3. **fetch_data Function:**
   - Connects to the SQL database using `pyodbc`.
   - Executes a provided SQL query to fetch data.
   - Writes the fetched data to a CSV file with specified headers.

4. **convert_excel Function:**
   - Converts a CSV file to an Excel file (`.xlsb` format) using Microsoft Excel application.
   - Saves the converted file and returns the new file name.

5. **main Flow:**
   - Fetches data from the SQL database using `fetch_data`.
   - Converts the fetched CSV file to `.xlsb` format using `convert_excel`.
   - Uploads the converted file to GCS using Google Cloud Storage client library.

6. **GCP Configuration:**
   - Uses a service account JSON file (`GCP_service.json`) for authentication with GCS.
   - Specifies the bucket name and folder where the file will be uploaded.


---
# Shoppers_combine.bat (combine_files.py)

#### Purpose:
The script `combine_files.py` is designed to convert Excel files to CSV format and combine them into a single DataFrame. It handles specific filtering for (SH) and (LS) data before saving the combined DataFrame to CSV files.

#### Main Components:

1. **Imports:**
   - Imports necessary modules (`time`, `win32com.client`, `pandas`, `get_files`, `os`).

2. **Global Variables:**
   - Defines the location for CSV files (`csv_location`) using the `get_files` module.

3. **convert Function:**
   - Converts Excel files to CSV format.
   - Handles multiple sheets within each Excel file and saves them as separate CSV files.
   - Returns a list of new CSV file names.

4. **HR_filter Function:**
   - Filters Shoppers Haryana stock data based on specific brands.

5. **combine Function:**
   - Combines multiple CSV files into a single DataFrame.
   - Handles different types of data (Shoppers Haryana and Lifestyle Sales).
   - Applies filters for specific columns (e.g., "Qty Available").
   - Saves the combined DataFrame to a CSV file.

6. **main Function:**
   - Calls `convert` to convert files.
   - Calls `combine` to combine and save the data based on the specified stock type (`SH` or `LS`).

7. **Example Usage:**
   - The script is designed to be run directly from the command line with predefined file paths and stock types.

---
# direct_send.py, email_send.py

I made this script to to be able to send logs via email. But sending email through SMTP requires it to be activated in the organization, which was not so I resorted to using a gmail account. Later I learned that I could send email without authentication and made a script called `direct_send.py`. It works by sending email via the organizations smtp server. One drawback is that all the email sent this will end up in spam folder. But that was not a problem for sending just logs.

#### Purpose:
The scripts `direct_send.py` and `email_send.py` are designed to send emails with HTML formatted content and optional attachments. They use SMTP authentication for Gmail or direct SMTP server communication.

#### Main Components:

1. **Email Sending Function:**
   - Both scripts contain a function `send_email(html, receiver_email, attachment=False)` which:
     - Constructs an email message.
     - Attaches an HTML body and optional files.
     - Sends the email using the specified SMTP server.

2. **HTML Conversion Function:**
   - Both scripts include a function `log_html(log)` that converts a log file into an HTML formatted string for easy viewing in email clients.

#### `direct_send.py`:

1. **Imports:**
   - Imports necessary modules (`smtplib`, `ssl`, `email`).

2. **Global Variables:**
   - Defines SMTP server details and sender credentials (though password is commented out).

3. **send_email Function:**
   - Constructs an email message with HTML content.
   - Attaches files if provided.
   - Uses a direct SMTP connection without authentication.

4. **log_html Function:**
   - Reads the contents of a log file and formats it into an HTML string.

5. **Example Usage:**
   - Demonstrates how to call `send_email` with an HTML message and attachments.

#### `email_send.py`:

1. **Imports:**
   - Imports necessary modules (`smtplib`, `ssl`, `email`).

2. **Global Variables:**
   - Defines SMTP server details for Gmail and sender credentials (password is required).

3. **send_email Function:**
   - Constructs an email message with HTML content.
   - Attaches files if provided.
   - Uses SMTP authentication to connect to the Gmail server.

4. **log_html Function:**
   - Reads the contents of a log file and formats it into an HTML string.

5. **Example Usage:**
   - Demonstrates how to call `send_email` with an HTML message, attachments, and a subject.
---

# kp_man.bat (key_partners_update_manual.py)

#### Purpose:
The script `key_partners_update_manual.py` automates the process of updating Key Partners sales and stock data to specific tables in an SQL database. It handles different types of files and requires manual intervention for processing.

#### Main Steps:

1. **Initialization:**
   - Imports necessary modules (`time`, `win32com.client`, `pandas`, `sql_con`, from `datetime` import `date`, `os`, `glob`).
   - Defines file paths, database connection, and SQL queries.
   - Establishes a connection to the SQL database using `sql_con.get_con("SDPD")`.

2. **File Paths and Data Definitions:**
   - Lists file paths for Blue Club sales, Kapsons sales, Kapsons stock, Lifestyle sales, Lifestyle stock, Shoppers sales, and Shoppers stock.

3. **Data Processing Functions:**

   - **HR_filter(df):**
     - Filters the Shoppers Haryana stock file based on specific brands.
   
   - **covert_to_csv(filenm, csv_location):**
     - Converts Excel files to CSV using Microsoft Excel application and saves them in a specified location.

   - **loading(filename, partner, table, cursor, sqlqi, dtype=None, header=0, parse_date=None, dayfirst=False, encoding='ansi')**
     - This is the main function that:
       - Filters and processes the file based on the type of data (Sales or Stock).
       - Reads the CSV files into pandas DataFrames.
       - Modifies the DataFrame according to its structure.
       - Deletes existing data from the target table.
       - Inserts new data into the target table using SQL queries.

4. **Loading Data:**
   - Calls the `loading` function multiple times for different partner files:
     - Kapsons Sales and Stock
     - Blue Club Sales
     - Lifestyle Sales and Stock
     - Shoppers Sales and Stock

5. **Cleanup:**
   - Closes the database connection.

#### External Dependencies:
- Uses functions from `sql_con`, `variable` modules, and `win32com.client` for file manipulation and SQL operations.
- Relies on external variables and configurations defined in other modules.

---

# kp.bat (key_partners_update.py)

This is same as the above one in terms of loading the data but fetching the excel data is automated. The `kp_variable_new.py` is the script which handles the fetching.

## kp_variable_new.py
#### Purpose:
The script `kp_variable_new.py` contains functions to check the existence of files and define file paths. It is essential for the `key_partners_update.py` script, which uses these paths to process and update data in SQL databases.

#### Main Components:

1. **Imports:**
   - Various Python libraries (`shutil`, `glob`, `os`, `datetime`, `re`) are imported for file manipulation and date calculations.

2. **Global Variables:**
   - Defines global variables for CSV locations, folder paths, dates, and other constants used throughout the script.

3. **Functions:**

   - **fnames(folder, kp_location=kp_location):**
     - Retrieves full paths of sales and stock files from a specified folder.
     - Uses regular expressions to filter file names based on patterns (e.g., "Sales" or "Stock").

   - **checkfiles(folder):**
     - Checks the existence of files in a specified folder using the `fnames` function.
     - If a particular file is not present, it uses backup files from another location and copies them to the current folder.
     - Returns lists of full paths for sales and stock files.

4. **File Paths:**
   - Defines paths for CSV locations (`csv_location`), key partner locations (`kp_location`), and backup locations (`bk_location`).

5. **Variable Definitions:**
   - Contains various variables used to define file paths, SQL queries, data types, and column lists for different types of data (e.g., sales, stock, Blue Club, Kapsons, Lifestyle, Shoppers Stop).

6. **SQL Queries:**
   - Includes SQL insert queries for different tables in the database (`blue_club_sales_sql`, `blue_club_stock_sqlq`, etc.).
---

# Online_DSR.py

#### Purpose:
The script `Online_DSR.py` processes an Excel file containing online DSR (Day Sales Report) data, converts it to CSV format, and then loads the data into a SQL database table. It also executes a stored procedure after loading the data.

#### Main Steps:

1. **Initialization:**
   - Logs the start time of the script execution.
   
2. **File Conversion:**
   - Converts an Excel file (`Online DSR.xlsb`) to a CSV file using Microsoft Excel application and saves it in the same directory with the `.csv` extension.

3. **Data Loading:**
   - Reads the converted CSV file into a pandas DataFrame.
   - Handles missing values by filling them with '1' for specific columns like `Net Unit`, `Net Value`, `GMV`, `Unit Sold`, and `Final GMV`.
   - Converts certain columns to string type.

4. **SQL Insert Query:**
   - Defines an SQL insert query to load data into the `Online_DSR_Bot` table in the `SSF.dbo` schema of the database.

5. **Loading Data into Database:**
   - Establishes a connection to the SQL database using `get_con('SSF')`.
   - Deletes existing data from the `Online_DSR_Bot` table.
   - Inserts new data into the table using pandas DataFrame values.
   - Calls a function `procedure.fill_null(df)` to handle null values in the DataFrame before inserting.

6. **Stored Procedure Execution:**
   - Executes a stored procedure `Online_DSR_Bot_SP` after loading the data.

7. **Cleanup:**
   - Closes the database connection.
   - Logs the total execution time of the script.

#### External Dependencies:
- Uses functions from `sql_con`, `procedure`, `process_data` modules, and `win32com.client` for file manipulation and SQL operations.
- Relies on external variables and configurations defined in other modules.

---

# update_SIS.py

#### Purpose:
The script `update_SIS.py` updates the SIS data by reading Excel files, processing them, and inserting the data into a SQL database. It also calculates and displays some summary statistics.

#### Main Steps:

1. **Initialization:**
   - Imports necessary modules (`queries`, `process_data`, `procedure`, `os`, `variable`, `datetime`, `pandas`, `sql_con`).
   - Establishes a connection to the SQL database using `sql_con.get_con('SSF')`.

2. **File Processing:**
   - Lists all files with the `.XLSX` extension in the specified location.
   - Reads each Excel file into a pandas DataFrame.

3. **Data Transformation:**
   - Converts the 'Date' column to a numeric index, adds 1899 (Excel date origin), and then formats it as '%d-%m-%Y'.
   - Filters the DataFrame to include only specified columns for sales data.
   - Calculates summary statistics like total sales amount, quantity, and net margin.

4. **Data Insertion:**
   - Truncates existing data in the target table (specified by `queries.sis_sales`).
   - Inserts new data into the target table using `process_data.sql_insert`.
   - Returns the start date of the processed data.

5. **Stored Procedure Execution:**
   - Executes a stored procedure (`Sales_Manual_SIS`) to update the database with the processed data.
   - Retrieves and prints sales summary by month.

6. **Cleanup:**
   - Closes the database connection.

#### External Dependencies:
- Uses functions from `queries`, `process_data`, and `procedure` modules for SQL operations, data processing, and file manipulation.
- Relies on external variables and configurations defined in other modules.
---

# VBRP.bat (VBRP_standalone.py)

#### Purpose:
The script `VBRP_standalone.py` updates data in a SQL database by reading from various sources, processing the data, and inserting it into specific tables. It handles different types of data sources and ensures proper formatting before insertion.

#### Main Steps:

1. **Initialization:**
   - Imports necessary modules (`time`, `sql_con`, `queries`, `variable`, `os`, `process_data`, `procedure`, `pandas`, `hdbcli`).
   - Establishes a connection to the SQL database using `sql_con.get_con("Sales_Source_Files")`.

2. **Data Retrieval:**
   - Retrieves data from an SAP HANA database table (`VBRP`) based on specific criteria.
   - Filters and processes the retrieved data to include only relevant columns.

3. **Insertion Function:**
   - Defines a function `insert_into` that takes parameters for the database connection, channel details, and file names.
   - Depending on the channel type:
     - Truncates existing data in the target table.
     - Reads data from files or retrieves it from SAP HANA.
     - Processes the data by replacing commas, converting dates, and filling null values.
     - Inserts the processed data into the target table using `process_data.sql_insert`.

4. **Data Processing:**
   - Applies specific processing steps for different channels (`vbrp`, `zfbl5n`, `inv_odn`).
   - For example, it handles numeric columns by removing commas and converting strings to datetime objects.

5. **File and Directory Operations:**
   - Lists files with specific extensions in a designated location.
   - Checks the existence of files before processing.

6. **Stored Procedure Execution:**
   - Executes a stored procedure (`VBRP_proc`) after loading the data, passing a date parameter ('2024-08-01').

7. **Cleanup:**
   - Closes the database connection.
   - Logs the total execution time of the script.

#### External Dependencies:
- Uses functions from `sql_con`, `queries`, `process_data`, and `procedure` modules for SQL operations, data processing, and file manipulation.
- Relies on external variables and configurations defined in other modules.

---

# zallocation.bat (zallocation.py)

#### Purpose:
The script `zallocation.py` automates the process of downloading, processing, and uploading data for ZAllocation. It handles file transfers from an FTP server, processes the data, inserts it into a SQL database, and then executes a stored procedure.

#### Main Steps:

1. **Initialization:**
   - Imports necessary modules (`time`, `auth`, `pandas`, `sql_con`, `procedure`, `ftplib`, `variable`, `glob`, `os`, `re`, `teams_msg`).
   - Establishes an FTP connection to the specified host and logs in with provided credentials.

2. **File Transfer:**
   - Changes the working directory on the FTP server.
   - Retrieves a list of files matching a specific pattern (`BD*_F2_*_<current_date>.xls`) and downloads them to a local directory.

3. **Database Connection:**
   - Establishes a connection to the SQL database using `sql_con.get_con("INVT")`.

4. **Data Processing:**
   - Defines columns that need numeric conversion.
   - Reads each downloaded CSV file into a pandas DataFrame.
   - Concatenates all DataFrames into a single DataFrame.
   - Drops the 'Brand Name' column if present.

5. **Insertion into Database:**
   - Truncates the target table in the database to remove existing data.
   - Inserts the processed data into the target table using `cursor.executemany`.
   - Handles batch inserts for efficiency by processing up to 25,000 rows at a time.

6. **Stored Procedure Execution:**
   - Executes a stored procedure (`ZAllocation_SSIS_Insert`) after loading the data.
   - Logs the output of the stored procedure to a CSV file.

7. **Cleanup:**
   - Closes the FTP connection and SQL cursor.
   - Logs the total execution time of the script.
   - Sends a notification message using `teams_msg.msg_teams`.

#### External Dependencies:
- Uses functions from `auth`, `sql_con`, `procedure`, `teams_msg` modules for authentication, database operations, and messaging.
- Relies on external variables and configurations defined in other modules.
---

# zpo.bat (zpo.py)

#### Purpose:
The script `zpo.py` handles the update of ZPO data by reading from CSV files, processing the data, and inserting it into a SQL database. It also executes stored procedures after the data insertion.

#### Main Steps:

1. **Initialization:**
   - Imports necessary modules (`time`, `sql_con`, `queries`, `process_data`, `procedure`, `os`, `variable`, `teams_msg`, `logging`).
   - Establishes logging configuration using a custom `log` function and logs the start of the process.

2. **File and Database Connections:**
   - Defines variables for file locations, log paths, and database connections.
   - Establishes a connection to the SQL database using `sql_con.get_con("Vendor")`.

3. **Data Processing Function:**
   - Defines a function `zpo` that:
     - Checks if the file exists.
     - Truncates existing data in the target table.
     - Reads and processes the CSV file, handling numeric conversions and cleaning specific columns.
     - Inserts the processed data into the target table using `process_data.sql_insert`.

4. **Main Processing:**
   - Logs the start of ZPO processing.
   - Calls the `zpo` function to update ZPO data.
   - If any error occurs during file processing, logs the error and sends a notification message.

5. **Stored Procedure Execution:**
   - Executes several stored procedures after loading the data:
     - A stored procedure specific to ZPO (`queries.zpo_tables['SP']`).
     - Week-to-date sell-thru update.
     - Weekly option sales category-season update with a date parameter ('2024-08-01').
     - Channel article sales update.

6. **Cleanup:**
   - Logs the completion of all operations and sends a notification message indicating load completion.
   - Closes the database connection.
   - Logs the total execution time of the script.

#### External Dependencies:
- Uses functions from `sql_con`, `queries`, `process_data`, and `procedure` modules for SQL operations, data processing, and file manipulation.
- Relies on external variables and configurations defined in other modules.
- Sends messages using `teams_msg.msg_teams` to notify users of completion or errors.
---

# zreport.bat (zreport.py)

#### Purpose:
The script `zreport.py` handles the update of ZMakt and ZOMNI data by reading from CSV files, processing the data, and inserting it into a SQL database. It uses parameterized queries to insert data.

#### Main Steps:

1. **Initialization:**
   - Imports necessary modules (`time`, `sql_con`, `queries`, `variable`, `os`, `process_data`, `procedure`, `pandas`).
   - Establishes the start time for performance measurement.
   - Establishes a connection to the SQL database using `sql_con.get_con("SSF")`.

2. **Data Processing Function:**
   - Defines a function `zrepot` that:
     - Checks if the file exists.
     - Truncates existing data in the target table.
     - Reads and processes the CSV file, handling numeric conversions and cleaning specific columns.
     - Inserts the processed data into the target table using `process_data.sql_insert`.

3. **Main Processing:**
   - Calls the `zrepot` function twice:
     - Once for ZMakt data (`queries.zmakt_table`, `variable.zmakt`, `queries.zmakt_insert`).
     - Once for ZOMNI data (`queries.zomni_table`, `variable.zomni`, `queries.zomni_insert`).

4. **Cleanup:**
   - Closes the database connection.
   - Logs the total execution time of the script.

#### External Dependencies:
- Uses functions from `sql_con`, `queries`, `process_data`, and `procedure` modules for SQL operations, data processing, and file manipulation.
- Relies on external variables and configurations defined in other modules.

