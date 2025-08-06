import shutil
import glob, os
from datetime import date as dt
from datetime import timedelta
import re


td = dt.today()
yt = td - timedelta(days = 1)
ytd = yt.strftime("%d.%m.%Y")
ytdmy = yt.strftime("%d-%m-%Y")
ytymd = yt.strftime("%Y-%m-%d")
tdymd = td.strftime("%Y-%m-%d")
tddmy = td.strftime("%d-%m-%Y")

botfile_location = r"\\BOT\Robotics_Automation\SIS\SIS_Report"
csv_location=r"C:\Users\USER\Documents\CSV"
bk_location = r"C:\Users\USER\Documents\Key_Partners"

kp_location = botfile_location+"\\"+tddmy
# kp_location = botfile_location+"\\"+"Archive\\28-12-2024"
csv_list = glob.glob(csv_location+"\\*")
for c in csv_list:
    os.remove(c)

def fnames(folder: str, kp_location:str=kp_location) -> list:
    fl = os.listdir(kp_location+"\\"+folder)
    stock = {re.sub("\d+\.[a-zA-Z]+",  "", i):i for i in fl if i.startswith("Stock")}
    return stock

def checkfiles(folder: str) -> list:
    if not os.path.exists(kp_location):
        old_stock = fnames(folder, bk_location)
        return old_stock
    new_stock = fnames(folder)
    old_stock = fnames(folder, bk_location)
    def check(x, y):
        files = []
        for a in y.keys():
            if a in x.keys():
                os.remove(bk_location+"\\"+folder+"\\"+y[a])
                shutil.copyfile(kp_location+"\\"+folder+"\\"+x[a], bk_location+"\\"+folder+"\\"+x[a])
                files.append(bk_location+"\\"+folder+"\\"+x[a])
                print(a)
            else: files.append(bk_location+"\\"+folder+"\\"+y[a])
        return files
    stock = check(new_stock, old_stock)
    return stock

Lifestyle_stock = checkfiles("Lifestyle")

Shoppers_stock = checkfiles("Shoppers Stop")

Shoppers_stock_JJ = checkfiles("Shoppers Stop\\JJ1")

Shoppers_stock_ON = checkfiles("Shoppers Stop\\ONLY")

Shoppers_stock_VM = checkfiles("Shoppers Stop\\VeroModa")

all_shopeprs_stock = Shoppers_stock+Shoppers_stock_JJ+Shoppers_stock_ON+Shoppers_stock_VM