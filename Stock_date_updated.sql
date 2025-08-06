declare @setDate as date;
set @setDate = format(GETDATE(), 'yyyy-MM-dd')

update [NPD].[dbo].[JJ_Closing_Report]
set Date = @setDate

update [NPD].[dbo].[Only and Sons_Closing_Report]
set Date = @setDate

update [NPD].[dbo].[Only_Closing_Report]
set Date = @setDate

update [NPD].[dbo].[Selected_Closing_Report]
set Date = @setDate

update [NPD].[dbo].[VM_Closing_Report]
set Date = @setDate

update [NPD].[dbo].[Jadeblue_Selected_Stock_SSIS]
set Date = @setDate

update [NPD].[dbo].[Jadeblue_JJ_Stock_SSIS]
set Date = @setDate

update [NPD].[dbo].[1J]
set Date = @setDate

update [NPD].[dbo].[1N]
set Date = @setDate

update [NPD].[dbo].[3V]
set Date = @setDate

update INVT.dbo.BrandFactory_Daily_Stock_SSIS
set Date = @setDate

update INVT.dbo.Central_Daily_Stock_SSIS
set Date = @setDate

update INVT.dbo.Kapsons_Daily_Stock_SSIS
set Date = @setDate

update INVT.dbo.Lifestyle_Daily_Stock_SSIS
set Date = @setDate

update [INVT].[dbo].[BLUECLUB_Daily_Stock_SSIS]
set Date = @setDate

update [INVT].[dbo].[Shoppers_Stop_Daily_Stock_SSIS]
set Date = @setDate