from __future__ import unicode_literals
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'sales.xlsx'
df_file=pd.read_excel(file)
#print(df_file)
#print (df_file['xdescr'])
#df_file.to_excel("sales_entry.xlsx")
sales_date=df_file['date']
sales_description=df_file['refer']+ df_file['description']
sales_amount=df_file['sales']
#print (sales_description)
vat=sales_amount*.05
total=sales_amount+vat
#df_all=pd.concat([sales_date,sales_description,sales_amount,vat,total],axis=1)
#df_all.to_excel("sales_entry.xlsx")

bank_debit= total
bank_credit=bank_debit*0
bank_account=bank_credit+12502
bank_desc=sales_description
bank_date= sales_date
bank_all=pd.concat([bank_debit,bank_credit,bank_account,bank_desc,bank_date],axis=1)

vat_credit=vat
vat_debit=vat_credit*0
vat_account=vat_debit+223
vat_desc= sales_description
vat_date= sales_date
vat_all=pd.concat([vat_debit,vat_credit,vat_account,vat_desc,vat_date],axis=1)
#df_all=pd.concat([bank_all,vat_all])
#df_all.to_excel("sales_entry.xlsx")

sales_credit=sales_amount
sales_debit=sales_credit*0
sales_account=sales_debit+41
sales_desc=vat_desc
sales_all=pd.concat([sales_debit,sales_credit,sales_account,sales_desc,sales_date],axis=1)

df_all=pd.concat([bank_all,vat_all,sales_all])
df_all.to_excel("sales_entry.xlsx")
