import time
start_time = time.time()
import win32com.client
from datetime import date
import pandas as pd
import get_files
import os


csv_location = get_files.csv_location

def convert(files):
    newnames = []
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Application.DisplayAlerts = False
    for k in files:
        if 'csv' in k:
            newnames.append(k)
            continue
        doc = excel.Workbooks.Open(k)
        v = doc.Sheets.Count
        for i in range(v):
            newname = csv_location+"\\"+k.split("\\")[-1]+str(i+1)+".csv"
            if os.path.exists(newname):
                newnames.append(newname)
                continue
            doc.Sheets(i+1).Select()
            newnames.append(newname)
            print(newname)
            doc.SaveAs(newname, 6)
            
        doc.Close(SaveChanges=False)
    return newnames

def HR_filter(df):
    df = df[df["Brand"].isin(["JJJ", "J&J", "ON", "VMM", "O-N", "VMI", 'VMG'])]
    return df

def combine(files, stock):
    df_dict = {}
    if stock == 'SH':
        for f in files:
            filename = f.split("\\")[-1]
            df = pd.read_csv(f, index_col=None, dtype=str, header=3, encoding='ansi')
            try:
                df.drop(['Unnamed: 16'], axis=1, inplace=True)
            except:
                pass
            df['FileName'] = filename
            print("--- %s seconds ---" % (time.time() - start_time))
            if "Stock_SS_HR" in filename:
                HR_filter(df)
            df_dict[filename] = df
            df.drop(df.tail(1).index,inplace=True)
            print(filename, "done")
        all_df = pd.concat(list(df_dict.values()), ignore_index=True)
        all_df = all_df.fillna('')
        all_df = all_df[all_df["Qty Available"] != '0']
        all_df = all_df[~all_df["Qty Available"].str.startswith("-")]
        all_df = all_df[~all_df['Partner \nPart No'].str.startswith("Total")]
        all_df = all_df[all_df['Brand'] != '']
        all_df.to_csv("C:/Users/USER/Documents/Output/SH.csv", index=False)
    elif stock == 'LS':
        for f in files:
            filename = f.split("\\")[-1]
            df = pd.read_csv(f, index_col=None, dtype=str, header=0, encoding='ansi')
            df['FileName'] = filename
            df_dict[filename] = df
            print(filename, "done")
            print("--- %s seconds ---" % (time.time() - start_time))
        all_df = pd.concat(list(df_dict.values()), ignore_index=True)
        all_df = all_df.fillna('')
        all_df.to_csv("C:/Users/USER/Documents/Output/LS.csv", index=False)



def main(files, stock):
    filenames = convert(files)
    combine(filenames, stock)

main(get_files.all_shopeprs_stock, 'SH')
main(get_files.LS_stock, 'LS')
