'''Contains all filename for channel and dates
Does Not contain any function
'''

from datetime import date as dt
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

td = dt.today()
yt = td - timedelta(days = 1)
ytd = yt.strftime("%d.%m.%Y")
ytymd = yt.strftime("%Y-%m-%d")
tdymd = td.strftime("%Y-%m-%d")
tddmy = td.strftime("%d-%m-%Y")
tdmdy = td.strftime("%m_%d_%Y")
tddmynu = td.strftime("%d%m%Y")
tddmy_ = td.strftime("%d_%m_%Y")
ytdmy_ = yt.strftime("%d_%m_%Y")

nmd = td + relativedelta(months=1)
nmd = nmd.replace(day=1)
lmd = nmd - relativedelta(days=1)
lmd = lmd.strftime("%Y-%m-%d")

lmfd = td -  relativedelta(months=1)
lmfd = lmfd.replace(day=1)
lmfd = lmfd.strftime("%Y-%m-%d")

location = r"D:\SAP_files"
log_loc = r"D:\SAP_files"
GCP_log_loc = "D:/Scripts/mssql_update/GCP/Log"

MTD_15 = "2025-02-01" 
ETL_rundate = '2024-08-01'
Outright_UG_rundate = '2025-03-01'
Online_18_rundate = '2025-03-01'

omni_files = ["OMNI 1.XLSX",
"OMNI 2.XLSX",
"OMNI 3.XLSX",
"OMNI 4.XLSX",
"OMNI 5.XLSX",
'OMNI 2022.XLSX',

# "OMNI 5.XLSX",
# "OMNI 6.XLSX",

# "OMNI 7.XLSX",
# "OMNI 2022.XLSX",
# "OMNI 8.XLSX",
# "OMNI 9.XLSX",
# "OMNI 10.XLSX",
# "OMNI 11.XLSX",
# 'OMNI 12.XLSX',
# 'OMNI 13.XLSX',
# 'OMNI 14.XLSX',
# 'OMNI 15.XLSX',
# 'OMNI 16.XLSX',
# 'OMNI 17.XLSX',
# 'OMNI 18.XLSX',
# 'OMNI 19.XLSX',
# 'OMNI 20.XLSX',
# 'OMNI 21.XLSX',
# 'OMNI 22.XLSX',
# 'OMNI 23.XLSX',
# 'OMNI 24.XLSX',
# 'OMNI 25.XLSX',
# 'OMNI 26.XLSX',
# 'OMNI 27.XLSX',
# 'OMNI 28.XLSX',
# 'OMNI 29.XLSX',
# 'OMNI 30.XLSX',
# 'OMNI 31.XLSX',
# 'OMNI 32.XLSX',
# 'OMNI 33.XLSX',
]

zpo_files = ['ZPO1.XLSX',
'ZPO2.XLSX',
'ZPO3.XLSX',
'ZPO4.XLSX',
'ZPO5.XLSX',
'ZPO6.XLSX',
'ZPO7.XLSX',
'ZPO8.XLSX',
'ZPO9.XLSX',
'ZPO10.XLSX',
'ZPO11.XLSX',
'ZPO12.XLSX',
'ZPO13.XLSX',
'ZPO14.XLSX',
'ZPO15.XLSX',
'ZPO16.XLSX',
'ZPO17.XLSX',
'ZPO18.XLSX',
'ZPO19.XLSX',
'ZPO20.XLSX'
]

tender_files = [
"Tender Recon 1.XLSX",
"Tender Recon 2.XLSX",
"Tender Recon 3.XLSX",
"Tender Recon 4.XLSX",
"Tender Recon 5.XLSX"
]

gatehold_invoice_files = [
"GATEHOLD INVOICE 2.XLSX",
"GATEHOLD INVOICE 3.XLSX",
"GATEHOLD INVOICE 4.XLSX",
"GATEHOLD INVOICE 5.XLSX",
"GATEHOLD INVOICE 6.XLSX",
"GATEHOLD INVOICE 7.XLSX",
"GATEHOLD INVOICE 8.XLSX",
"GATEHOLD INVOICE.XLSX",
"GATEHOLD INVOICE 9.XLSX",
"GATEHOLD INVOICE 10.XLSX"
]

gatein = ["GATEIN.XLSX"]
gateout = ["GATEOUT.XLSX"]
gatehold_delivery = ["GATEHOLD DELIVERY.XLSX"]

scrap = ["SCRAP & INSTITUTIONAL.XLSX"]
outright = ["OUTRIGHT.XLSX"]
online_or = ["Online Outright (ZGST_OUTWARD2).XLSX"]
produkt = ["PRODUKT.XLSX"]
export = ["EXPORT.XLSX"]
zsis = ["ZSIS (1).XLSX"]

dc_stock = ["BS01 Stock.txt",
            "BS02 Stock.txt"]

dc_stock_columns = ['Column 0',	' Typ ',	'Stor Bin',	'Log Pos',	'Resource',	'TU Int',	'TU',	'Carrier',	'HU           ',	'Product   ',
		    	'Product Short Description               ',	'Quantity',	'BUn',	'ST',	'Desc Stock Type            ',	'Batch',	'RU',	'Origin',	'Owner',	
				'Ent toDisp',	'Use',	'Tpe',	'SlsOrd Prj',	'SlsOrd Itm',	'InspType',	'Q  Insp   ',	'Expiration',	'GR Time ',	'GR Date   ',	'IA',	
				'StBinImp',	'Cert  No ',	'PSA',	'Cat',	'AvlQtyAUoM',	'AUn',	'   Counter',	'Column 37'
]

zmakt = [
"ZMAKT_1.XLSX",
"ZMAKT_2.XLSX",
"ZMAKT_3.XLSX",
"ZMAKT_4.XLSX",
"ZMAKT_5.XLSX",
"ZMAKT_6.XLSX",
"ZMAKT_7.XLSX",
"ZMAKT_8.XLSX",
"ZMAKT_9.XLSX",
"ZMAKT_10.XLSX",
"ZMAKT_11.XLSX",
"ZMAKT_12.XLSX",
"ZMAKT_13.XLSX",
"ZMAKT_14.XLSX",
"ZMAKT_15.XLSX",
"ZMAKT_16.XLSX",
"ZMAKT_17.XLSX",
"ZMAKT_18.XLSX",
"ZMAKT_19.XLSX",
"ZMAKT_20.XLSX"
]

zomni = [
"CAPTIVE_YTD_1.XLSX",
"CAPTIVE_YTD_2.XLSX",
"CAPTIVE_YTD_3.XLSX",
"CAPTIVE_YTD_4.XLSX",
"CAPTIVE_YTD_5.XLSX",
"CAPTIVE_YTD_6.XLSX",
"CAPTIVE_YTD_7.XLSX",
"CAPTIVE_YTD_8.XLSX",
"CAPTIVE_YTD_9.XLSX",
"CAPTIVE_YTD_10.XLSX",
"CAPTIVE_YTD_11.XLSX",
"CAPTIVE_YTD_12.XLSX",
"CAPTIVE_YTD_13.XLSX",
"CAPTIVE_YTD_14.XLSX",
"CAPTIVE_YTD_15.XLSX",
"CAPTIVE_YTD_16.XLSX",
"CAPTIVE_YTD_17.XLSX",
"CAPTIVE_YTD_18.XLSX",
"CAPTIVE_YTD_19.XLSX",
"CAPTIVE_YTD_20.XLSX"
]

vbrp = ['VBRP_VRPMA.XLSX']
zfbl5n = ['Ledger.XLSX']
inv_odn = ['inv_map.XLSX']

uploads = "D:/Scripts/mssql_update/GCP/"