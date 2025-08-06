'''This is the main file containing all the things related to tables, like SQL insert queries,
SQL SP, Dates, column order, table names, date_parsing
There are no functions inside
'''

import variable

inv_odn_insert = '''
INSERT INTO [Sales_Source_Files].[dbo].[Inv_ODN]

values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

zfbl5n_insert = '''
INSERT INTO [Sales_Source_Files].[dbo].[zfbl5n]

values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

vbrp_insert = '''
INSERT INTO [Sales_Source_Files].[dbo].[VBRP_VRPMA]
		
values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

uni_insert = '''
INSERT INTO [Sales_Source_Files].[dbo].[Unicommerce_bestseller]

values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
)
'''


zmakt_insert = '''
	INSERT INTO [Sales_Source_Files].[dbo].[zmakt_track]

	  values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
	  ?,?,?,?,?,?,?,?,?,?,?,?,?

)

'''

zomni_insert = '''
INSERT INTO [Sales_Source_Files].[dbo].[zomni_track]


	values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
)
'''

manual_sis = '''
INSERT INTO [Sales_Source_Files].[dbo].[Manual_SIS]


	  values(?,?,?,?,?,?,?,?,?)
'''

zpo_insert = ''' INSERT INTO [Vendor].[dbo].[ZPO_Track_Temp_1]

	  values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

'''

dc_stock_insert = ''' INSERT INTO [INVT].[dbo].[Bhiwandi Stock_temp]
	
		values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

'''

zsis_insert = '''
INSERT INTO [Dim].[dbo].[zsis_temp_table]
      
      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
      
'''

online_18_insert = '''
INSERT INTO [FACT].[dbo].[Outright_20-21]
      
      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

gatehold_delivery_insert = '''
INSERT INTO [INVT_W].[dbo].[GateHold_Weekly_SSIS]
      
      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

gatehold_invoice_insert = '''
INSERT INTO [INVT_W].[dbo].[Gatehold_Invoice_Weeky_SSIS]
      
      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

gateout_insert = '''
INSERT INTO [INVT_W].[dbo].[GateOUT_Weekly_SSIS]
      
      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

gatein_insert = '''
INSERT INTO [INVT_W].[dbo].[GateIN_Weekly_SSIS]
      
      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''


tender_insert = '''
INSERT INTO [Ageing].[dbo].[Alltender_fbl3n_temp]
      
      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
	  )
      
'''


outright_insert = '''
INSERT INTO [SSIS_Upload].[dbo].[Sales_Outright_UG]
      
      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
)
'''


Omni_insert    = '''
INSERT INTO Sales_Omni

      values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
)
'''
def outward_insert(table):
	outward_insert = f'''
	INSERT INTO {table}
		
		values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
	)
	'''
	return outward_insert

omni_clean = '''
insert into ssis_upload.[dbo].[Sales_Omni_Final]
Select 
	ltrim(rtrim(Cust_order_Number)) Cust_order_Number,
	ltrim(rtrim(Cust_Line_item)) Cust_Line_item,
	ltrim(rtrim(Order_Item)) Order_Item,
	ltrim(rtrim(SAP_Order_Number)) SAP_Order_Number,
	ltrim(rtrim(SAP_Line_Item)) SAP_Line_Item,
	case 
		when SO_Date like '%[a-z]%' then cast(convert(varchar,SO_Date,6) as date)
		when SO_Date = null then cast(Null as date)
		else Datefromparts(right(SO_Date,4),SUBSTRING(SO_Date,4,2), left(SO_Date,2))
	end SO_Date,
	ltrim(rtrim(Payment_Method)) Payment_Method,
	ltrim(rtrim(Customer_Name)) Customer_Name,
	ltrim(rtrim(City_Name)) City_Name,
	ltrim(rtrim(Forward_PIN_Code)) Forward_PIN_Code,
	ltrim(rtrim(Forward_Address)) Forward_Address,
	ltrim(rtrim(State)) State,
	ltrim(rtrim(Mobile_F_)) Mobile_F_,
	ltrim(rtrim(Category)) Category,
	ltrim(rtrim(Sub_Category)) Sub_Category,
	ltrim(rtrim(Brand)) Brand,
	ltrim(rtrim(Payer)) Payer,
	ltrim(rtrim(Payer_Name)) Payer_Name,
	ltrim(rtrim(Shipper)) Shipper,
	ltrim(rtrim(Issuing_DC)) Issuing_DC,
	ltrim(rtrim(RSO_Manual_Action)) RSO_Manual_Action,
	Case 
		when replace(replace(replace(SO_MRP,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SO_MRP,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SO_MRP,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SO_MRP,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SO_MRP,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SO_MRP,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(SO_MRP,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(SO_MRP,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(SO_MRP,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SO_MRP,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(SO_MRP,' ',''),'"',''),',','') as decimal(18,8)) 
	end SO_MRP,
	Case 
		when replace(replace(replace(SO_Discount,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SO_Discount,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SO_Discount,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SO_Discount,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SO_Discount,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SO_Discount,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(SO_Discount,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(SO_Discount,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(SO_Discount,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SO_Discount,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(SO_Discount,' ',''),'"',''),',','') as decimal(18,8)) 
	end SO_Discount,
	Case 
		when replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(SO_Discount_Percen,' ',''),'"',''),',','') as decimal(18,8)) 
	end SO_Discount_Percen,
	Case 
		when replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(SO_Partner_MRP,' ',''),'"',''),',','') as decimal(18,8)) 
	end SO_Partner_MRP,
	Case 
		when replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(SO_Net_Sales,' ',''),'"',''),',','') as decimal(18,8)) 
	end SO_Net_Sales,
	Case 
		when replace(replace(replace(SO_CGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SO_CGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SO_CGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SO_CGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SO_CGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SO_CGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(SO_CGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(SO_CGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(SO_CGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SO_CGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(SO_CGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end SO_CGST,
	Case 
		when replace(replace(replace(SO_SGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SO_SGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SO_SGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SO_SGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SO_SGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SO_SGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(SO_SGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(SO_SGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(SO_SGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SO_SGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(SO_SGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end SO_SGST,
	Case 
		when replace(replace(replace(SO_IGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SO_IGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SO_IGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SO_IGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SO_IGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SO_IGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(SO_IGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(SO_IGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(SO_IGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SO_IGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(SO_IGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end SO_IGST,
	ltrim(rtrim(Rejection_Reason)) Rejection_Reason,
	ltrim(rtrim(Article)) Article,
	ltrim(rtrim(EAN)) EAN,
	ltrim(rtrim(Quantity)) Quantity,
	ltrim(rtrim(Delivery_Number)) Delivery_Number,
	ltrim(rtrim(Delivery_Item_Number)) Delivery_Item_Number,
	ltrim(rtrim(LSP_Code)) LSP_Code,
	ltrim(rtrim(LSP_Name)) LSP_Name,
	ltrim(rtrim(Forward_AWB)) Forward_AWB,
	ltrim(rtrim(Forward_AWB_Status)) Forward_AWB_Status,
	case 
		when Customer_Del_date like '%[a-z]%' then cast(convert(varchar,Customer_Del_date,6) as date)
		when Customer_Del_date = null then cast(Null as date)
		else Datefromparts(right(Customer_Del_date,4),SUBSTRING(Customer_Del_date,4,2), left(Customer_Del_date,2))
	end Customer_Del_date,
	ltrim(rtrim(Invoice)) Invoice,
	ltrim(rtrim(ACE_Invoice)) ACE_Invoice,
	Case 
		when Invoice_Date like '%[a-z]%' then cast(convert(varchar,Invoice_Date,6) as date)
		when Invoice_Date = null then cast(Null as date)
		else Datefromparts(right(Invoice_Date,4),SUBSTRING(Invoice_Date,4,2), left(Invoice_Date,2))
	end Invoice_Date,
	ltrim(rtrim(Invoice_item_Number)) Invoice_item_Number,
	Case 
		when replace(replace(replace(Invoice_MRP,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Invoice_MRP,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Invoice_MRP,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Invoice_MRP,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Invoice_MRP,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Invoice_MRP,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Invoice_MRP,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Invoice_MRP,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Invoice_MRP,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Invoice_MRP,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Invoice_MRP,' ',''),'"',''),',','') as decimal(18,8)) 
	end Invoice_MRP,
	Case 
		when replace(replace(replace(Invoice_Discount,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Invoice_Discount,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Invoice_Discount,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Invoice_Discount,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Invoice_Discount,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Invoice_Discount,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Invoice_Discount,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Invoice_Discount,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Invoice_Discount,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Invoice_Discount,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Invoice_Discount,' ',''),'"',''),',','') as decimal(18,8)) 
	end Invoice_Discount,
	Case 
		when replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Invoice_Discount_Percen,' ',''),'"',''),',','') as decimal(18,8)) 
	end Invoice_Discount_Percen,
	Case 
		when replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Invoice_Partner_MRP,' ',''),'"',''),',','') as decimal(18,8)) 
	end Invoice_Partner_MRP,
	Case 
		when replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Invoice_Net_Sales,' ',''),'"',''),',','') as decimal(18,8)) 
	end Invoice_Net_Sales,
	Case 
		when replace(replace(replace(Invoice_CGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Invoice_CGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Invoice_CGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Invoice_CGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Invoice_CGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Invoice_CGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Invoice_CGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Invoice_CGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Invoice_CGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Invoice_CGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Invoice_CGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end Invoice_CGST,
	Case 
		when replace(replace(replace(Invoice_SGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Invoice_SGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Invoice_SGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Invoice_SGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Invoice_SGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Invoice_SGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Invoice_SGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Invoice_SGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Invoice_SGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Invoice_SGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Invoice_SGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end Invoice_SGST,
	Case 
		when replace(replace(replace(Invoice_IGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Invoice_IGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Invoice_IGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Invoice_IGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Invoice_IGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Invoice_IGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Invoice_IGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Invoice_IGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Invoice_IGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Invoice_IGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Invoice_IGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end Invoice_IGST,
	ltrim(rtrim(Return_Order)) Return_Order,
	ltrim(rtrim(RSO_Created_By)) RSO_Created_By,
	ltrim(rtrim(Return_SAP_Line_Item)) Return_SAP_Line_Item,
	ltrim(rtrim(Return_Cust_Line_Item)) Return_Cust_Line_Item,
	case 
		when Return_Order_Date like '%[a-z]%' then cast(convert(varchar,Return_Order_Date,6) as date)
		when Return_Order_Date = null then cast(Null as date)
		else Datefromparts(right(Return_Order_Date,4),SUBSTRING(Return_Order_Date,4,2), left(Return_Order_Date,2))
	end Return_Order_Date,
	ltrim(rtrim(Return_Payer_Code)) Return_Payer_Code,
	ltrim(rtrim(Return_Payer_Name)) Return_Payer_Name,
	ltrim(rtrim(Bank_Account_Name)) Bank_Account_Name,
	ltrim(rtrim(Bank_Name)) Bank_Name,
	ltrim(rtrim(Account_Number)) Account_Number,
	ltrim(rtrim(IFSC_Code)) IFSC_Code,
	ltrim(rtrim(Pickup_PIN_Code)) Pickup_PIN_Code,
	ltrim(rtrim(Pickup_Address)) Pickup_Address,
	ltrim(rtrim(Pickup_State)) Pickup_State,
	ltrim(rtrim(Return_Delivery)) Return_Delivery,
	ltrim(rtrim(Return_LSP_Code)) Return_LSP_Code,
	ltrim(rtrim(Return_LSP_Name)) Return_LSP_Name,
	ltrim(rtrim(Return_Delivery_Item)) Return_Delivery_Item,
	ltrim(rtrim(Return_AWB)) Return_AWB,
	case 
		when Customer_Ret_Del_Date like '%[a-z]%' then cast(convert(varchar,Customer_Ret_Del_Date,6) as date)
		when Customer_Ret_Del_Date = null then cast(Null as date)
		else Datefromparts(right(Customer_Ret_Del_Date,4),SUBSTRING(Customer_Ret_Del_Date,4,2), left(Customer_Ret_Del_Date,2))
	end Customer_Ret_Del_Date,
	case 
		when Credit_Memo_Date like '%[a-z]%' then cast(convert(varchar,Credit_Memo_Date,6) as date)
		when Credit_Memo_Date = null then cast(Null as date)
		else Datefromparts(right(Credit_Memo_Date,4),SUBSTRING(Credit_Memo_Date,4,2), left(Credit_Memo_Date,2))
	end Credit_Memo_Date,
	ltrim(rtrim(Credit_Memo)) Credit_Memo,
	ltrim(rtrim(Credit_Memo_Item)) Credit_Memo_Item,
	Case 
		when replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Credit_Memo_MRP,' ',''),'"',''),',','') as decimal(18,8)) 
	end Credit_Memo_MRP,
	Case 
		when replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Credit_Memo_Discount,' ',''),'"',''),',','') as decimal(18,8)) 
	end Credit_Memo_Discount,
	Case 
		when replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Credit_Memo_Discount_Percen,' ',''),'"',''),',','') as decimal(18,8)) 
	end Credit_Memo_Discount_Percen,
	Case 
		when replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Credit_Memo_Partner_MRP,' ',''),'"',''),',','') as decimal(18,8)) 
	end Credit_Memo_Partner_MRP,
	Case 
		when replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Credit_Memo_Net_Sales,' ',''),'"',''),',','') as decimal(18,8)) 
	end Credit_Memo_Net_Sales,
	Case 
		when replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Credit_Memo_CGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end Credit_Memo_CGST,
	Case 
		when replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Credit_Memo_SGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end Credit_Memo_SGST,
	Case 
		when replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when right(replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',',''),1) = '-' then cast(replace(replace(replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',',''),'-',''),')','') as decimal(18,8))*-1
		when left(replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,8))*-1
		else cast(replace(replace(replace(Credit_Memo_IGST,' ',''),'"',''),',','') as decimal(18,8)) 
	end Credit_Memo_IGST,
	ltrim(rtrim(Status)) Status,
ltrim(rtrim([Final Status])) [Final Status],
[Ordering Store],
[Fulfilling Store], 
null as [Quantity_1], 
null as [Invoice_MRP_1], 
null as [Invoice_Discount_1], 
null as [Invoice_Net_Sales_1], 
null as [Invoice_CGST_1],
null as [Invoice_SGST_1], 
null as [Invoice_IGST_1],
[Ref Stat],
ltrim(rtrim([Return AWB Status])),
ltrim(rtrim([Myntra packet id])),
ltrim(rtrim([Business Channel])),
ltrim(rtrim([Return order type])),
ltrim(rtrim([Spf Ticket Id])),
ltrim(rtrim([Issue Category])),
ltrim(rtrim([Ticket Status])),
Case 
		when [Recovery Date] like '%[a-z]%' then cast(convert(varchar,[Recovery Date],6) as date)
		when [Recovery Date] = null then cast(Null as date)
		else Datefromparts(right([Recovery Date],4),SUBSTRING([Recovery Date],4,2), left([Recovery Date],2))
	end [Recovery Date],
null as [Ticket Raise Date],
ltrim(rtrim([Approved Amount])),
ltrim(rtrim([Cust order new]))
from ssis_upload.[dbo].[Sales_Omni];

'''

scrap_clean = '''

Insert into Sales_Scrap_Final 
Select 
[Company Code] as Company_Code,
[Business Place] as Business_Place,
[Site] as Supply_site_Code,
[Site Description] as Supply_site_Name,
[Supply Site City] as Supply_site_City,
[Site Region] as GST_Supp_region_code,
[Site Region Description] as Text_Region_in_which_site_is_located,
[Site GST No] as Supply_site_GSTIN_NO,
[Payer] as Payer,
[Payer Description] as Text_Payer,
[Bill-To Party] as Bill_to_party,
[Bill-To Description] as Text_Bill_to_party,
[Bill-To City] as Bill_to_party_City,
[Bill-To Region] as GST_Reg_Cd,
[Region Description] as Bill_to_party_Region,
[GST No] as GSTIN_NO_Bill_to_party,
[Ship-To Party] as Ship_to_party,
[Ship-To Description] as Text_Ship_to_party,
[Ship-To City] as Ship_to_party_City,
[Region] as Ship_to_party_Region_Code,
[Region Description] as Ship_to_party_Region,
[GST no#] as Ship_to_party_GSTIN,
[Sales Type] as Sales_Type_intra_inter_export_,
[Bill-to Reg/Unreg] as Bill_to_Party_Registered_Unregistered_,
datefromparts(right([Invoice Date],4),substring([Invoice Date],4,2),left([Invoice Date],2)) as Invoice_date, 
datefromparts(right([Accounting Date],4),substring([Accounting Date],4,2),left([Accounting Date],2)) as Accounting_date,
[Accounting No] as Accounting_Doc_No,
[Billing Doc#] as Billing_Document,
[Original Inv No#] as Reference_Invoice_No,
null as Reference_Invoice_No_1,
[Original Inv ODN] as Original_Invoice_Reference_No,
[Cancel Doc#] as Cancel_Doc,
[Tcode] as Tcode,
[Billing Type] as Billing_Type,
[Billing Type Desc] as Billing_Type_Description,
[HSN] as HSN_NO,
[Article] as Article,
[Article Desc] as Article_Description,
[Merchandise Catg Desc] as Mdse_Catgry_Desc,
[Brand Desc] as Brand_Name,
[Posting Status] as Posting_Status,
Case 
		when replace(replace(replace([Quantity],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Quantity],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Quantity],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Quantity],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Quantity],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Quantity],' ',''),'"',''),',','') as decimal(18,5)) 
	end Actual_invoiced_quantity_,
Case 
		when replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Current MRP],' ',''),'"',''),',','') as decimal(18,5)) 
	end Transaction_MRP,
Case 
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Net Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end Basic_Net_sales_,
Case 
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Net Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end Basic_Net_sales_INR_,
Case 
		when replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([CGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end CGST_AMT,
Case 
		when replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([SGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end SGST_UGST_AMT,
Case 
		when replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([IGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end IGST_AMT,
Case 
		when replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Gross Total],' ',''),'"',''),',','') as decimal(18,5)) 
	end Gross_Total_INR_,
Case 
		when replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([CGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end CGSTpercen,
Case 
		when replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([SGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end SGST_UGSTpercen,
Case 
		when replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([IGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end IGSTpercen

,[Net GL Account]	 as    Net_Amount_G_L_A_C_Number
,[Net Account Name]	  as   Net_Amount_G_L_A_C_Name
,[Distribution Channel]	 as Distribution_Channel
,[CGST GL Account]	as CGST_G_L_A_C_Number
,[CGST Account Name] as	CGST_GL_A_C_Name
,[SGST GL Account]	as SGST_G_L_A_C_Number
,[SGST Account Name] as	SGST_GL_A_C_Name
,[IGST GL Account]	as IGST_G_L_A_C_Number
,[IGST Account Name]	as IGST_GL_A_C_Name
,Case 
		when replace(replace(replace(Cost,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Cost,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Cost,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Cost,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Cost,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Cost,' ',''),'"',''),',','') as decimal(18,5)) 
	end Cost,

	null as Exchange_rate_accntg,
[Purchase Order No#] as Purchase_order_number,
null as Sales_Document,
null as Reference_document
from [scrap-outward2];

'''

produkt_clean = '''

Insert into Sales_Produkt_Final
Select 
[Company Code] as Company_Code,
[Business Place] as Business_Place,
[Site] as Supply_site_Code,
[Site Description] as Supply_site_Name,
[Supply Site City] as Supply_site_City,
[Site Region] as GST_Supp_region_code,
[Site Region Description] as Text_Region_in_which_site_is_located,
[Site GST No] as Supply_site_GSTIN_NO,
[Payer] as Payer,
[Payer Description] as Text_Payer,
[Bill-To Party] as Bill_to_party,
[Bill-To Description] as Text_Bill_to_party,
[Bill-To City] as Bill_to_party_City,
[Bill-To Region] as GST_Reg_Cd,
[Region Description] as Bill_to_party_Region,
[GST No] as GSTIN_NO_Bill_to_party,
[Ship-To Party] as Ship_to_party,
[Ship-To Description] as Text_Ship_to_party,
[Ship-To City] as Ship_to_party_City,
[Region] as Ship_to_party_Region_Code,
[Region Description] as Ship_to_party_Region,
[GST no#] as Ship_to_party_GSTIN,
[Sales Type] as Sales_Type_intra_inter_export_,
[Bill-to Reg/Unreg] as Bill_to_Party_Registered_Unregistered_,
datefromparts(right([Invoice Date],4),substring([Invoice Date],4,2),left([Invoice Date],2)) as Invoice_date, 
datefromparts(right([Accounting Date],4),substring([Accounting Date],4,2),left([Accounting Date],2)) as Accounting_date,
[Accounting No] as Accounting_Doc_No,
[Billing Doc#] as Billing_Document,
[Original Inv No#] as Reference_Invoice_No,
null as Reference_Invoice_No_1,
[Original Inv ODN] as Original_Invoice_Reference_No,
[Cancel Doc#] as Cancel_Doc,
[Tcode] as Tcode,
[Billing Type] as Billing_Type,
[Billing Type Desc] as Billing_Type_Description,
[HSN] as HSN_NO,
[Article] as Article,
[Article Desc] as Article_Description,
[Merchandise Catg Desc] as Mdse_Catgry_Desc,
[Brand Desc] as Brand_Name,
[Posting Status] as Posting_Status,
Case 
		when replace(replace(replace([Quantity],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Quantity],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Quantity],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Quantity],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Quantity],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Quantity],' ',''),'"',''),',','') as decimal(18,5)) 
	end Actual_invoiced_quantity_,
Case 
		when replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Current MRP],' ',''),'"',''),',','') as decimal(18,5)) 
	end Transaction_MRP,
Case 
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Net Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end Basic_Net_sales_,
Case 
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Net Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end Basic_Net_sales_INR_,
Case 
		when replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([CGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end CGST_AMT,
Case 
		when replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([SGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end SGST_UGST_AMT,
Case 
		when replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([IGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end IGST_AMT,
Case 
		when replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Gross Total],' ',''),'"',''),',','') as decimal(18,5)) 
	end Gross_Total_INR_,
Case 
		when replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([CGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end CGSTpercen,
Case 
		when replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([SGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end SGST_UGSTpercen,
Case 
		when replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([IGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end IGSTpercen

,[Net GL Account]	 as    Net_Amount_G_L_A_C_Number
,[Net Account Name]	  as   Net_Amount_G_L_A_C_Name
,[Distribution Channel]	 as Distribution_Channel
,[CGST GL Account]	as CGST_G_L_A_C_Number
,[CGST Account Name] as	CGST_GL_A_C_Name
,[SGST GL Account]	as SGST_G_L_A_C_Number
,[SGST Account Name] as	SGST_GL_A_C_Name
,[IGST GL Account]	as IGST_G_L_A_C_Number
,[IGST Account Name]	as IGST_GL_A_C_Name
,Case 
		when replace(replace(replace(Cost,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Cost,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Cost,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Cost,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Cost,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Cost,' ',''),'"',''),',','') as decimal(18,5)) 
	end Cost,

	null as Exchange_rate_accntg,
[Purchase Order No#] as Purchase_order_number,
null as Sales_Document,
null as Reference_document
from dbo.[Produkt-outward2]
where [Invoice Date] is not null


'''

outright_clean = f'''

Insert Into Sales_Outright_UG_Final 
Select 
Company_Code,
Business_Place,
Supply_site_Code,
Supply_site_Name,
Supply_site_City,
GST_Supp_region_code,
Text_Region_in_which_site_is_located,
Supply_site_GSTIN_NO,
Payer,
Text_Payer,
Bill_to_party,
Text_Bill_to_party,
Bill_to_party_City,
GST_Reg_Cd,
Bill_to_party_Region,
GSTIN_NO_Bill_to_party,
Ship_to_party,
Text_Ship_to_party,
Ship_to_party_City,
Ship_to_party_Region_Code,
Ship_to_party_Region,
Ship_to_party_GSTIN,
Sales_Type_intra_inter_export_,
Bill_to_Party_Registered_Unregistered_,
convert(date,Invoice_date,104) as Invoice_date,
convert(date,accounting_date,104) as accounting_date,
Accounting_Doc_No,
Billing_Document,
Reference_Invoice_No,
Reference_Invoice_No_1,
Original_Invoice_Reference_No,
Cancel_Doc,
Tcode,
Billing_Type,
Billing_Type_Description,
HSN_NO,
Article,
Article_Description,
Mdse_Catgry_Desc,
Brand_Name,
Posting_Status,
Case 
		when replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Actual_invoiced_quantity_,' ',''),'"',''),',','') as decimal(18,5)) 
	end Actual_invoiced_quantity_,
Case 
		when replace(replace(replace(Transaction_MRP,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Transaction_MRP,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Transaction_MRP,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Transaction_MRP,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Transaction_MRP,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Transaction_MRP,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Transaction_MRP,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Transaction_MRP,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Transaction_MRP,' ',''),'"',''),',','') as decimal(18,5)) 
	end Transaction_MRP,
Case 
		when replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Basic_Net_sales_,' ',''),'"',''),',','') as decimal(18,5)) 
	end Basic_Net_sales_,
Case 
		when replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Basic_Net_sales_INR_,' ',''),'"',''),',','') as decimal(18,5)) 
	end Basic_Net_sales_INR_,
Case 
		when replace(replace(replace(CGST_AMT,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(CGST_AMT,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(CGST_AMT,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(CGST_AMT,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(CGST_AMT,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(CGST_AMT,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(CGST_AMT,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(CGST_AMT,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(CGST_AMT,' ',''),'"',''),',','') as decimal(18,5)) 
	end CGST_AMT,
Case 
		when replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(SGST_UGST_AMT,' ',''),'"',''),',','') as decimal(18,5)) 
	end SGST_UGST_AMT,
Case 
		when replace(replace(replace(IGST_AMT,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(IGST_AMT,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(IGST_AMT,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(IGST_AMT,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(IGST_AMT,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(IGST_AMT,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(IGST_AMT,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(IGST_AMT,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(IGST_AMT,' ',''),'"',''),',','') as decimal(18,5)) 
	end IGST_AMT,
Case 
		when replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Gross_Total_INR_,' ',''),'"',''),',','') as decimal(18,5)) 
	end Gross_Total_INR_,
Case 
		when replace(replace(replace(CGSTpercen,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(CGSTpercen,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(CGSTpercen,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(CGSTpercen,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(CGSTpercen,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(CGSTpercen,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(CGSTpercen,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(CGSTpercen,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(CGSTpercen,' ',''),'"',''),',','') as decimal(18,5)) 
	end CGSTpercen,
Case 
		when replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(SGST_UGSTpercen,' ',''),'"',''),',','') as decimal(18,5)) 
	end SGST_UGSTpercen,
Case 
		when replace(replace(replace(IGSTpercen,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(IGSTpercen,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(IGSTpercen,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(IGSTpercen,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(IGSTpercen,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(IGSTpercen,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(IGSTpercen,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(IGSTpercen,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(IGSTpercen,' ',''),'"',''),',','') as decimal(18,5)) 
	end IGSTpercen,
Net_Amount_G_L_A_C_Number,
Net_Amount_G_L_A_C_Name,
Distribution_Channel,
CGST_G_L_A_C_Number,
CGST_GL_A_C_Name,
SGST_G_L_A_C_Number,
SGST_GL_A_C_Name,
IGST_G_L_A_C_Number,
IGST_GL_A_C_Name,
Case 
		when replace(replace(replace(Cost,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Cost,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Cost,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Cost,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Cost,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Cost,' ',''),'"',''),',','') as decimal(18,5)) 
	end Cost,
Case 
		when replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Exchange_rate_accntg,' ',''),'"',''),',','') as decimal(18,5)) 
	end Exchange_rate_accntg,
Purchase_order_number,
Sales_Document,
Reference_document
from Sales_Outright_UG;

delete from FACT.dbo.Sales_Outright_UG
		where Invoice_Date >= '{variable.MTD_15}'
		and Invoice_Date<=(select max(date) from FACT.dbo.sales_UG_manual) ;

'''

export_clean = '''

Insert into Sales_Export_Final
Select 
[Company Code] as Company_Code,
[Business Place] as Business_Place,
[Site] as Supply_site_Code,
[Site Description] as Supply_site_Name,
[Supply Site City] as Supply_site_City,
[Site Region] as GST_Supp_region_code,
[Site Region Description] as Text_Region_in_which_site_is_located,
[Site GST No] as Supply_site_GSTIN_NO,
[Payer] as Payer,
[Payer Description] as Text_Payer,
[Bill-To Party] as Bill_to_party,
[Bill-To Description] as Text_Bill_to_party,
[Bill-To City] as Bill_to_party_City,
[Bill-To Region] as GST_Reg_Cd,
[Region Description] as Bill_to_party_Region,
[GST No] as GSTIN_NO_Bill_to_party,
[Ship-To Party] as Ship_to_party,
[Ship-To Description] as Text_Ship_to_party,
[Ship-To City] as Ship_to_party_City,
[Region] as Ship_to_party_Region_Code,
[Region Description] as Ship_to_party_Region,
[GST no#] as Ship_to_party_GSTIN,
[Sales Type] as Sales_Type_intra_inter_export_,
[Bill-to Reg/Unreg] as Bill_to_Party_Registered_Unregistered_,
datefromparts(right([Invoice Date],4),substring([Invoice Date],4,2),left([Invoice Date],2)) as Invoice_date, 
datefromparts(right([Accounting Date],4),substring([Accounting Date],4,2),left([Accounting Date],2)) as Accounting_date,
[Accounting No] as Accounting_Doc_No,
[Billing Doc#] as Billing_Document,
[Original Inv No#] as Reference_Invoice_No,
null as Reference_Invoice_No_1,
[Original Inv ODN] as Original_Invoice_Reference_No,
[Cancel Doc#] as Cancel_Doc,
[Tcode] as Tcode,
[Billing Type] as Billing_Type,
[Billing Type Desc] as Billing_Type_Description,
[HSN] as HSN_NO,
[Article] as Article,
[Article Desc] as Article_Description,
[Merchandise Catg Desc] as Mdse_Catgry_Desc,
[Brand Desc] as Brand_Name,
[Posting Status] as Posting_Status,
Case 
		when replace(replace(replace([Quantity],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Quantity],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Quantity],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Quantity],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Quantity],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Quantity],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Quantity],' ',''),'"',''),',','') as decimal(18,5)) 
	end Actual_invoiced_quantity_,
Case 
		when replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Current MRP],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Current MRP],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Current MRP],' ',''),'"',''),',','') as decimal(18,5)) 
	end Transaction_MRP,
Case 
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Net Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end Basic_Net_sales_,
Case 
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Net Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Net Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Net Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end Basic_Net_sales_INR_,
Case 
		when replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([CGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([CGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([CGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end CGST_AMT,
Case 
		when replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([SGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([SGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([SGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end SGST_UGST_AMT,
Case 
		when replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([IGST Amount],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([IGST Amount],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([IGST Amount],' ',''),'"',''),',','') as decimal(18,5)) 
	end IGST_AMT,
Case 
		when replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([Gross Total],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([Gross Total],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([Gross Total],' ',''),'"',''),',','') as decimal(18,5)) 
	end Gross_Total_INR_,
Case 
		when replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([CGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([CGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([CGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end CGSTpercen,
Case 
		when replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([SGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([SGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([SGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end SGST_UGSTpercen,
Case 
		when replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace([IGST Rate],' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace([IGST Rate],' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace([IGST Rate],' ',''),'"',''),',','') as decimal(18,5)) 
	end IGSTpercen

,[Net GL Account]	 as    Net_Amount_G_L_A_C_Number
,[Net Account Name]	  as   Net_Amount_G_L_A_C_Name
,[Distribution Channel]	 as Distribution_Channel
,[CGST GL Account]	as CGST_G_L_A_C_Number
,[CGST Account Name] as	CGST_GL_A_C_Name
,[SGST GL Account]	as SGST_G_L_A_C_Number
,[SGST Account Name] as	SGST_GL_A_C_Name
,[IGST GL Account]	as IGST_G_L_A_C_Number
,[IGST Account Name]	as IGST_GL_A_C_Name
,Case 
		when replace(replace(replace(Cost,' ',''),'"',''),',','') = '-' then 0.00
		when replace(replace(replace(Cost,' ',''),'"',''),',','') = '(blank)' then 0.00
		when  left(replace(replace(replace(Cost,' ',''),'"',''),',',''),1) = '#' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') = 'NULL' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') = '' then 0.00
		when  replace(replace(replace(Cost,' ',''),'"',''),',','') like '%[a-z]%' then 0.00
		when left(replace(replace(replace(Cost,' ',''),'"',''),',',''),1) = '(' then cast(replace(replace(replace(replace(replace(Cost,' ',''),'"',''),',',''),'(',''),')','') as decimal(18,5))*-1
		else cast(replace(replace(replace(Cost,' ',''),'"',''),',','') as decimal(18,5)) 
	end Cost,

	null as Exchange_rate_accntg,
[Purchase Order No#] as Purchase_order_number,
null as Sales_Document,
null as Reference_document
from dbo.[Export-outward2]
where [Invoice Date] is not null

'''


Outright_columns = ["Company Code",	"Business Place",	"Site",	"Site Description",	"Supply Site City",	"Site Region",
			"Site Region Description",	"Site GST No",	"Payer",	"Payer Description",	"Bill-To Party",
					"Bill-To Description",	"Bill-To City",	"Bill-To Region",	"Region Description",	
					"GST No",	"Ship-To Party",	"Ship-To Description",	"Ship-To City",	"Region",	
					"Region Description",	"GST no.",	"Sales Type",	"Bill-to Reg/Unreg",	
					"Invoice Date",	"Accounting Date",	"Accounting No",	"Billing Doc.",	"Original Inv No.",
							"Reference_Invoice_No_1",	"Original Inv ODN",	"Cancel Doc.",	"Tcode",	
							"Billing Type",	"Billing Type Desc",	"HSN",	"Article",	"Article Desc",	
							"Merchandise Catg Desc",	"Brand Desc",	"Posting Status",	"Quantity",	
							"Current MRP",	"Basic_Net_sales_",	"Net Amount",	"CGST Amount",	"SGST Amount",	
							"IGST Amount",	"Gross Total",	"CGST Rate",	"SGST Rate",	"IGST Rate",	
							"Net GL Account",	"Net Account name",	"Distribution Channel",	"CGST GL Account",	
							"CGST Account Name",	"SGST GL Account",	"SGST Account Name",	
							"IGST GL Account",	"IGST Account Name",	"Cost",	"Exchange_rate_accntg",	
							"Purchase Order No.",	"Sales_Document",	"Reference_document"
]

Online_18_columns = ['Company Code',	'Business Place',	'Site',	'Site Description',	'Supply Site City',	'Site Region',	'Site Region Description',	
		     'Site GST No',	'Payer',	'Payer Description',	'Bill-To Party',	'Bill-To Description',	'Bill-To City',	'Bill-To Region',	
			 'Region Description',	'GST No',	'Ship-To Party',	'Ship-To Description',	'Ship-To City',	'Region',	'Region Description',	
			 'GST no.',	'Sales Type',	'Bill-to Reg/Unreg',	'Invoice Date',	'Accounting Date',	'Accounting No',	'Billing Doc.',	
			 'Original Inv No.',	'ODN',	'Original Inv ODN',	'Cancel Doc.',	'Tcode',	'Billing Type',	'Billing Type Desc',	'HSN',	'Article',	
			 'Article Desc',	'Merchandise Catg Desc',	'Brand Desc',	'Posting Status',	'Quantity',	'Current MRP',	'Basic (Net sales)',	
			 'Net Amount',	'CGST Amount',	'SGST Amount',	'IGST Amount',	'Gross Total',	'CGST Rate',	'SGST Rate',	'IGST Rate',	'Net GL Account',	
			 'Net Account name',	'Distribution Channel',	'CGST GL Account',	'CGST Account Name',	'SGST GL Account',	'SGST Account Name',	
			 'IGST GL Account',	'IGST Account Name',	'Cost',	'Exchange rate-accntg',	'Purchase Order Number',	'Sales Document',	'Reference Document',
]

Online_18_dates_columns = ['Invoice Date',	'Accounting Date']

outright_ug_sap_SP = f'''EXEC [FACT].[dbo].[Sales_SAP] @FromDate = '{variable.Outright_UG_rundate}',@ToDate = '{variable.ytymd}',@DF = N'OutrightUG' '''

omni_sap_SP = f''' EXEC [FACT].[dbo].[Sales_SAP] @FromDate = '{variable.ETL_rundate}',@ToDate = '{variable.ytymd}',@DF = N'Omni' '''

scrap_sap_SP = f'''EXEC [FACT].[dbo].[Sales_SAP] @FromDate = '{variable.MTD_15}',@ToDate = '{variable.ytymd}',@DF = N'Scrap' '''

produkt_sap_SP = f''' EXEC [FACT].[dbo].[Sales_SAP] @FromDate = '{variable.MTD_15}',@ToDate = '{variable.ytymd}',@DF = N'Produkt' '''

export_sap_SP = f'''EXEC [FACT].[dbo].[Sales_SAP] @FromDate = '{variable.MTD_15}',@ToDate = '{variable.ytymd}',@DF = N'Export' '''

omni_tables = {'delete':"Sales_Omni", 'final':"Sales_OMNI_Final", 'insert':omni_clean, 'SP':omni_sap_SP}
scrap_tables = {'delete':'[SSIS_Upload].[dbo].[scrap-outward2]','final':'Sales_Scrap_Final', 'insert':scrap_clean, 'SP':scrap_sap_SP}
produkt_table = {'delete':"[SSIS_Upload].[dbo].[Produkt-outward2]", 'final':'Sales_Produkt_Final', 'insert':produkt_clean, 'SP':produkt_sap_SP}
outright_table = {'delete':"Sales_Outright_UG", 'final':"Sales_Outright_UG_Final", 'insert':outright_clean, 'SP':outright_ug_sap_SP, 'columns': Outright_columns,
		  'add':['Reference_Invoice_No_1', "Basic_Net_sales_", "Exchange_rate_accntg", "Sales_Document", "Reference_document"]}
export_table  = {'delete':"SSIS_Upload.dbo.[Export-outward2]", 'final':"Sales_Export_Final", 'insert':export_clean, 'SP':export_sap_SP}

online_18_table = {'delete':f''' delete from FACT.[dbo].[Outright_20-21] where  [Accounting Date] >= '{variable.Online_18_rundate}' ''',
		   'insert': online_18_insert, 'SP': ''' delete b from FACT.dbo.[Outright_20-21] b
		where [Invoice Date] >=(select min(date) from FACT.dbo.SALES_ONLINE_Outright)
		and [Invoice Date]<=(select max(date) from FACT.dbo.SALES_ONLINE_Outright) ''', 
		'add': ['Basic (Net sales)', 'Exchange rate-accntg',	'Purchase Order Number',	'Sales Document',	'Reference Document'],
		   'columns':Online_18_columns, 'dates':Online_18_dates_columns
		   }

zpo_sp = ''' update Vendor.dbo.ZPO_Track_Temp_1 set [Expected Arrival Date] = null where [Expected Arrival Date] like '%1899%'; EXEC Vendor.[dbo].[ZPO_Track_Proc_2] '''

zpo_tables = {'name':'ZPO', 'delete': '[Vendor].[dbo].[ZPO_Track_Temp_1]', 'SP':zpo_sp}

zmakt_num = ['Quantity',	'SO CGST',	'SO SGST',	'SGST COD',	'IGST COD',	'SO Partner MRP',	'SO IGST',	'SO_Date',	'SO Discount',	'SO Discount %',	
			 'Credit Memo MRP',	'Credit Memo Discount',	'Credit Memo Discount %',	'Credit Memo Partner MRP',	'Credit Memo IGST',	'Invoice CGST',	'CGST SHP',	
			 'Total Tax Amt',	'SGST SHP',	'IGST SHP',	'COD Charges',	'CGST COD',	'Invoice SGST',	'Invoice IGST',	'Shipping Charges',	'Total Inv (Incl. Tax)',	
			 'SO Shipping Charges',	'SO COD Charges',	'Invoice MRP',	'Invoice Discount',	'Invoice Discount %',	'Invoice Partner MRP',	'Invoice Net Sales',	
			 'Credit Memo Net Sales',	'Credit Memo CGST',	'Credit Memo SGST',	'SO Net Sales'
]

zomni_num = ['Quantity',	'SO MRP',	'SO Discount',	'SO Discount %',	'SO Partner MRP',	'SO Net Sales',	'SO Shipping Charges',	'SO COD Charges',	
			 'SO Tender - Bluedart',	'SO Tender - Delhivery',	'SO Tender - CC Avenue',	'SO Tender - Phone Pay',	'SO Tender - ANS GV',	'SO Tender -  ANS Money',	
			 'SO CGST',	'SO SGST',	'SO IGST',	'Delivery Quantity',	'Inv. MRP',	'Inv. Discount',	'Inv. Discount %',	'Inv. Partner MRP',	'Inv. Amt(Tax incl)',	
			 'SHP Charges',	'COD Charges',	'Inv. Total(Tax incl)',	'INV Tender - Bluedart',	'INV Tender - Delhivery',	'INV Tender -  CC Avenue',	'INV Tender - Phone Pay',	
			 'INV Tender -  ANS GV',	'INV Tender -  ANS Money',	'Inv. CGST',	'Inv. SGST',	'Inv. IGST',	'SHP CGST',	'SHP SGST',	'SHP IGST',	'Return Delivery Quantity',	
			 'Credit Memo MRP',	'Credit Memo Discount',	'Credit Memo Discount %',	'Credit Memo Partner MRP',	'Total Credit(Tax incl)',	'Credit Memo Tender - Cashfree',	
			 'Credit Memo Tender - Bluedart',	'Credit Memo Tender - Delhivery',	'Credit Memo Tender - CC Avenue',	'Credit Memo Tender - Phone Pay',	
			 'Credit Memo Tender - ANS GV',	'Credit Memo Tender - ANS Money',	'Credit Memo CGST',	'Credit Memo SGST',	'Credit Memo IGST',	'Refundable Amount'
]

zmakt_dates = ['Cust Order Date',	'Customer Ret Del Date',	'SO_Date',	'Credit Memo Date',	'Return Order Date',	'Customer Del date',	'Invoice Date',	'TAT Date',
			   'Ticket Raise Date', 'Recovery Date']
zomni_dates = ['SO Sales Date',	'SO Posting Date',	'Customer Del date',	'Inv. Date',	'Cust RSO date',	'SAP RSO Date',	'Customer Ret Del Date',	'Credit Memo Date',	
			   'Refund Initiated Date',	'Refund Date',	'Manual Ref App Date',	'Fwd Pick Up Date',]
zmakt_cl = ['Business Channel',	'Issuing DC',	'Cust order new',	'Category',	'Sub Category',	'Cust Line item',	'SAP Order Number',	'Article',	'EAN',	'Delivery Number',	
			'Cust Ref Number',	'Customer Name',	'City Name',	'SAP Line Item',	'Forward PIN Code',	'SO_Time',	'Forward Address',	'State',	'Mobile(F)',	
			'Return SAP Line Item',	'Return Cust Line Item',	'Pickup City',	'Pickup State',	'Pickup Cust Name',	'RSO Created By',	'Pickup Address',	'Pickup PIN Code',	
			'Return Delivery',	'Return Delivery Item',	'Return AWB',	'Return AWB Status',	'AWB Error (LSP)',	'AWB Error (Pretr)',	'Partner Invoice',	
			'Delivery Item Number',	'Brand',	'Payer',	'Payer Name',	'Payment Method',	'SO MRP',	'Credit Memo',	'Credit Memo Item',	'Detailed Status',	
			'Final Status',	'TO Confirm',	'Return Order',	'Return Payer Code',	'LSP Code',	'LSP Name',	'Forward AWB',	'Forward AWB Status',	'Shipper',	'Invoice',	
			'TAT Time',	'Invoice item Number',	'HU Number',	'TO Number',	'TO Item',	'Storage Type',	'Storage BIN',	'Return Payer Name',	'Rejection Reason',	
			'Return id',	'Myntra packet id',	'Cust order Number',
]

zomni_cl = ['Business Channel',	'Posting Time',	'Cust order Number',	'Cust Line item',	'Order-Item',	'SAP Order Number',	'SAP Line Item',	'Company Code',	'Issuing DC',	
			'ISTO No',	'ISTO Line Item',	'ISTO Site',	'ISTO Delivery',	'ISTO Delivery line Item',	'ISTO Pack St.',	'ISTO PGI St.',	'Article',	'EAN',	'Category',	
			'Sub Category',	'Brand',	'Customer Name',	'City Name',	'Forward PIN Code',	'Forward Address',	'State',	'Mobile(F)',	'Email(F)',	'Payer',	
			'Payer Name',	'Payment Method',	'Shipper',	'Delivery Number',	'Delivery Item Number',	'LSP Code',	'LSP Name',	'Forward AWB',	'Forward AWB Status',	
			'Invoice',	'Inv. item Number',	'RSO Manual Action',	'Rejection Reason',	'Rej Reason Text',	'DC Cancelled Response (ANS)',	'Return Order',	'RSO Created By',	
			'Return SAP Line Item',	'Return Cust Line Item',	'Return Payer Code',	'Return Payer Name',	'Bank Account Name',	'Bank Name',	'Account Number',	
			'IFSC Code',	'Pickup Cust Name',	'Pickup Address',	'Pickup City',	'Pickup PIN Code',	'Pickup State',	'Return Delivery',	'Return LSP Code',	
			'Return LSP Name',	'Return Delivery Item',	'Return AWB',	'Return AWB Status',	'AWB Error (LSP)',	'AWB Error (ANS)',	'Credit Memo',	'Credit Memo Item',	
			'Dummy Order No.',	'Forward Tenders',	'Return/Cancel Tenders',	'Refund Initiated',	'Refund Processed',	'Status',	'Final Status',	'Duplicate',	
			'Manual Ref Eligibilty',	'Ref Eligibilty',	'Ref Stat',
]

uni_cl = ['Sale Order Item Code',	'Display Order Code',	'Reverse Pickup Code',	'Reverse Pickup Reason',	'Notification Email',	'Notification Mobile',	
		  'Require Customization',	'COD',	'Shipping Address Id',	'Category',	'Invoice Code',	'Invoice Created',	'EWayBill No',	'Shipping Address Name',	
		  'Shipping Address Line 1',	'Shipping Address Line 2',	'Shipping Address City',	'Shipping Address State',	'Shipping Address Country',	
		  'Shipping Address Pincode',	'Shipping Address Phone',	'Billing Address Id',	'Billing Address Name',	'Billing Address Line 1',	'Billing Address Line 2',	
		  'Billing Address City',	'Billing Address State',	'Billing Address Country',	'Billing Address Pincode',	'Billing Address Phone',	'Shipping Method',	
		  'Item SKU Code',	'Channel Product Id',	'Item Type Name',	'Item Type Color',	'Item Type Size',	'Item Type Brand',	'Channel Name',	'SKU Require Customization',	
		  'Gift Wrap',	'Gift Message',	'HSN Code',	'MRP',	'Total Price',	'Selling Price',	'Cost Price',	'Prepaid Amount',	'Subtotal',	'Discount',	'GST Tax Type Code',	
		  'CGST',	'IGST',	'SGST',	'UTGST',	'CESS',	'CGST Rate',	'IGST Rate',	'SGST Rate',	'UTGST Rate',	'CESS Rate',	'TCS Amount',	'Tax %',	'Tax Value',	
		  'Voucher Code',	'Shipping Charges',	'Shipping Method Charges',	'COD Service Charges',	'Gift Wrap Charges',	'Packet Number',	'Sale Order Code',	'On Hold',
		  'Sale Order Status',	'Priority',	'Currency',	'Currency Conversion Rate',	'Sale Order Item Status',	'Cancellation Reason',	'Shipping provider',	'Shipping Courier',	
		  'Shipping Arranged By',	'Shipping Package Code',	'Shipping Package Status Code',	'Shipping Package Type',	'Length(mm)',	'Width(mm)',	'Height(mm)',	
		  'Delivery Time',	'Tracking Number',	'Facility',	'Return Reason',	'Combination Identifier',	'Combination Description',	'Transfer Price',	'Item Code',	
		  'IMEI',	'Weight',	'GSTIN',	'Customer GSTIN',	'TIN',	'Payment Instrument',	'Fulfillment TAT',	'Adjustment In Selling Price',	'Adjustment In Discount',	
		  'Store Credit',	'IRN',	'Acknowledgement Number',	'Bundle SKU Code Number',	'SKU Name',	'Batch Code',	'Vendor Batch Number',	'Seller SKU Code',	
		  'Item Type EAN',	'Shipping Courier Status',	'Shipping Tracking Status',	'Item Seal Id',	'Parent Sale Order Code',	'BOXNUMBER',	'ORDER_DELNO',	
		  'ORDER_DELITEMNO',	'STORAGEBIN',	'DC',	'RRP',	'AjioBasePrice',	'WAVENUMBER',	'I_SALESORDER',	'DelNum',	'Sale Order Item Code.1',	
		  'Packet ID Myntra',	'Channel Shipping',	'Item Details']

zmakt_table = {'name':'ZMAKT', 'delete': '[Sales_Source_Files].[dbo].[zmakt_track]', 'num': zmakt_num, 'dates': zmakt_dates, 'cl': zmakt_cl}
zomni_table = {'name':'ZOMNI', 'delete': '[Sales_Source_Files].[dbo].[zomni_track]', 'num': zomni_num, 'dates': zomni_dates, 'cl': zomni_cl}

vbrp_num = ['Billed Quantity', 'Subtotal 1', 'Subtotal 2', 'Subtotal 3', 'Subtotal 4', 'Subtotal 5', 'Exch.Rate', 'Tax amount', 'Gross value', 'Net value']
vbrp_dates = ['Billing Date', 'Created On']

vbrp = {'name':'VBRP', 'delete': '[Sales_Source_Files].[dbo].[VBRP_VRPMA]', 'num': vbrp_num, 'dates': vbrp_dates, 'insert': vbrp_insert}

zfbl5n_num = ['Amount in Doc. curr', 'Amount in loc. curr', 'ZW/RV QTY', 'Realised sales price']
zfbl5n_dates = ['Posting Date', 'Document Date', 'Entry Date', 'PO/SO/RSO Doc Date', 'PO Date', 'Delviery Date', 'ZW/RV LR Date', 'Act Delivery Date']

zfbl5n = {'name':'zfbl5n', 'delete': '[Sales_Source_Files].[dbo].[zfbl5n]', 'num': zfbl5n_num, 'dates': zfbl5n_dates, 'insert': zfbl5n_insert}

inv_odn_dates = ['Billing Date', 'Created On']

inv_odn = {'name':'inv_odn', 'delete': '[Sales_Source_Files].[dbo].[Inv_ODN]', 'num': False, 'dates': inv_odn_dates, 'insert': inv_odn_insert}

uni_dates = ['Reverse Pickup Created Date', 'Invoice Created', 'EWayBill Date', 'EWayBill Valid Till', 'Order Date as dd/mm/yyyy hh:MM:ss', 'Shipping Package Creation Date',
         'Dispatch Date','Return Date', 'Created', 'Updated', 'Fulfillment TAT', ]

uni_table = {'name':'Unicommerce_bestseller', 'delete': '[Sales_Source_Files].[dbo].[Unicommerce_bestseller]','dates': uni_dates, 'base_insert': uni_insert, 'cl': uni_cl}

sis_columns = ['New Store',	'Chain',	'Store name',	'Brand',	'Region',	'real_date',	'Sum of Sale',	'Sum of Sale QTY',	'Sum of Margin Ach']
sis_sales = {'name': 'SIS', 'delete': ''' [Sales_Source_Files].[dbo].[Manual_SIS] ''', 'columns': sis_columns}

zsis_SP = "EXEC Dim.[dbo].[customer_master_Proc]"
zsis = {'name': "zsis", 'delete': "Dim.[dbo].[zsis_temp_table]", 'SP': zsis_SP}

tender = {'delete':'''[Ageing].[dbo].[Alltender_fbl3n_temp]''',
	  'name':'TENDER',
'insert':'''
exec Ageing.[dbo].TRDN;

EXEC Ageing.dbo.ODD '2021-04-01';

EXEC Ageing.dbo.DUS;

EXEC Ageing.dbo.DU;

'''}

dc_stock = {'delete': "[INVT].[dbo].[Bhiwandi Stock_temp]", 'name': "DC_STOCK"}

dc_stock_SP = f''' [INVT].dbo.Bhiwandi_Stock_Insert '{variable.ytymd}' '''

gatein = {'name':'Gatein',
	  'delete':''' delete  FROM [INVT_W].[dbo].[GateIN_Weekly_SSIS] where Convert(Date,[System Gate Entry date],104)>= '2019-09-01' ''',
	  'insert':gatein_insert, 'add':["GR_Done", "Inward_Pendency_Days"], 'columns': False,
	  'dates': False}

gateout_columns = ['Gate out number',	'Creation Date',	'Month',	'Material',	'STO/SO type',	'Purchase Order',	'Sales Order',	'STO/SO Date',	'Brand ID',
		   	'Brand Description',	'Supplying Site',	'Company Name',	'Supplying City',	'Store Code',	'Store Name',	'Store City',	'State',	'ODN',	
			'Delivery No',	'Actual GI Date',	'Invoice No',	'Invoice Date',	'Month',	'Qty',	'Inv Amt',	'Cartons',	'Ewaybill',	'Outward Date',	
			'Outward Time',	'Gatepass No',	'Lsp name',	'Bill Of Lading/AWB No',	'Act Delivery Date',	'Api Status Date',	'Commited Date',	
			'Commited Days',	'Transporter Inv No',	'Delivery Document Date',	'Charged Weight',	'Vehicle No',	'Driver name',	'Driver Phone no',	
			'Any Remark',	'Delivery Document Done',	'Diff_Inv_date',	'Outward_Pendency_Days',	'Delivery Status',	'Invoice Status'
]
gateout_date_columns = ['Creation Date', 'STO/SO Date', 'Actual GI Date', 'Act Delivery Date',
			'Commited Date', 'Delivery Document Date']

gateout = {'name':'Gateout', 'delete':f''' delete  FROM [INVT_W].[dbo].[GateOUT_Weekly_SSIS] where [Creation Date] >= '{variable.MTD_15}' ''',
		'insert': gateout_insert, 'add':["Delivery Document Done", "Diff_Inv_date", "Outward_Pendency_Days"],
		'columns': gateout_columns, 'dates': gateout_date_columns
	   }

gatehold_invoice_columns = ['Brand',	'Invoice Number',	'PGI date',	'Delivery Document date',	'Invoice Date',	'Store/Partner Code',	'ODN   Number',	
			    'Delivery Number',	'CPO Delivery Number',	'SO/STO',	'Plant',	'Supplying Site Name',	'Supplying City',	'Store/Partner Name',	
				'Store/Partner City',	'Store/Partner State',	'Quantity',	'Amount'
]

gatehold_invoice_date_columns = ['PGI date', 'Delivery Document date', 'Invoice Date']

gatehold_invoice = {'name':'gatehold_invoice', 'delete':'''truncate table [INVT_W].[dbo].[Gatehold_Invoice_Weeky_SSIS]''',
		    'insert': gatehold_invoice_insert, 'add':False, 'columns': gatehold_invoice_columns, 'dates': gatehold_invoice_date_columns
		    }

gatehold_delivery_columns = ['STO No',	'SO No',	'Brand',	'STO/SO Delivery',	'PGI Date',	'Packing Date',	'Delivery Document Date',	
			     'Store/Partner Code',	'Warehouse Number',	'Supplying Site',	'Supplying Site Name',	'Supplying State',	'Store/Partner Name',	
				 'Store/Partner City',	'Store/Partner State',	'Packing Qty',	'Actual Scan Qty',	'CPO Delivery'
]

gatehold_delivery_date_columns = ['PGI Date',	'Packing Date',	'Delivery Document Date']

gatehold_delivery = {'name':'gatehold_delivery', 'delete':'''  truncate table [INVT_W].[dbo].[GateHold_Weekly_SSIS] ''',
		     'insert': gatehold_delivery_insert, 'add':False, 'columns': gatehold_delivery_columns, 'dates': gatehold_delivery_date_columns
}

outward_pendency_SP = f'''EXEC [INVT_W].[dbo].[Outward_pendency] @date = '{variable.tdymd}' '''

stock_OH = f''' EXEC [INVT_W].[dbo].[SISONLINE_STOCK] @date = '{variable.ytymd}' '''

insert_V2 = f''' Exec [INVT_W].[dbo].[INSERT_v2] '{variable.ytymd}' '''

D2 = f'''EXEC [FACT].[dbo].[D2] @DF = N'All',@date = '{variable.ETL_rundate}' '''

D3 = f''' EXEC [FACT].[dbo].[D3] @FromDate ='{variable.ytymd}' --Today-1'''
#SxD3_new SxD3_t
D4 = f'''EXEC [FACT].[dbo].[D4] @date ='{variable.ETL_rundate}' --YTD Week  first monday of september'''

D5 = '''EXEC [FACT].[dbo].[D5]'''

D6 = f'''EXEC [FACT].[dbo].[D6] @date ='{variable.ETL_rundate}' --YTD'''

lastweek = '''EXEC [FACT].[dbo].[4WEEK]'''

lastweek_V2 = '''EXEC [FACT].[dbo].[4WEEKV2]  -------Run this store procedure on a daily basis'''

monthly_trends = '''FACT.[dbo].[MONTHLY_T]'''

main_insert = f''' EXEC [INVT_W].[dbo].Sales_INSERT @Date='{variable.ytymd}' '''

bucket = ''' EXEC [INVT_W].[dbo].WEEKLY_BUCKET '''

fc_daily_sales = f" exec FACT.[dbo].[FC_DAILY] '{variable.ETL_rundate}' "

onoos_stock = " exec [INVT_W].dbo.[ON] "

WB1 = "EXEC [Finance].[dbo].[WB_SP] '2023-08-01','2023-08-31','Jul'"

WB2 = "EXEC [Finance].[dbo].[WB_SP] '2023-09-01','2023-09-30','Aug' "

WB3 = "EXEC [Finance].[dbo].[WB_SP] '2023-10-01','2023-10-31','Sep' "

WB4 = "EXEC [Finance].[dbo].[WB_SP] '2023-11-01','2023-11-30','Oct' "

WB5 = "EXEC [Finance].[dbo].[WB_SP] '2023-12-01','2023-12-31','Nov' "

WB6 = "EXEC [Finance].[dbo].[WB_SP] '2024-01-01','2024-01-31','Dec' "
 
WB7 = "EXEC [Finance].[dbo].[WB_SP] '2024-02-01','2024-02-29','Jan' "

WB8 = "EXEC [Finance].[dbo].[WB_SP] '2024-03-01','2024-03-31','Feb' "

WB9 = "ExEC [Finance].[dbo].[WB_SP] '2024-04-01','2024-04-30','Mar' "

WB10 = "ExEC [Finance].[dbo].[WB_SP] '2024-05-01','2024-05-31','Apr' "

WB11 = "ExEC [Finance].[dbo].[WB_SP] '2024-06-01','2024-06-30','May' "

WB12 = "ExEC [Finance].[dbo].[WB_SP] '2024-07-01','2024-07-31','Jun' "

WB13 = "ExEC [Finance].[dbo].[WB_SP] '2024-08-01','2024-08-31','JulNY' "

WB14 = "ExEC [Finance].[dbo].[WB_SP] '2024-09-01','2024-09-30','AugNY' "

WB15 = "ExEC [Finance].[dbo].[WB_SP] '2024-10-01','2024-10-31','SepNY' "

WB16 = "ExEC [Finance].[dbo].[WB_SP] '2024-11-01','2024-11-30','OctNY' "

WB17 = "ExEC [Finance].[dbo].[WB_SP] '2024-12-01','2024-12-31','NovNY' "

WB18 = "ExEC [Finance].[dbo].[WB_SP] '2025-01-01','2025-01-31','DecNY' "