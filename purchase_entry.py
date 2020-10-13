from __future__ import unicode_literals
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'purchases.xlsx'
df_file=pd.read_excel(file)
#print(df_file)
#print (df_file['xdescr'])
#df_file.to_excel("purchases_entry.xlsx")
purchases_date=df_file['date']
purchases_description=df_file['refer']+ df_file['description']
purchases_amount=df_file['purchases']
#print (purchases_description)
vat=purchases_amount*.05
total=purchases_amount+vat
#df_all=pd.concat([purchases_date,purchases_description,purchases_amount,vat,total],axis=1)
#df_all.to_excel("purchases_entry.xlsx")


bank_credit=total
bank_debit= bank_credit*0
bank_account=bank_debit+12502
bank_desc=purchases_description
bank_date= purchases_date
bank_all=pd.concat([bank_debit,bank_credit,bank_account,bank_desc,bank_date],axis=1)


vat_debit=vat
vat_credit=vat_debit*0
vat_account=vat_credit+223
vat_desc= purchases_description
vat_date= purchases_date
vat_all=pd.concat([vat_debit,vat_credit,vat_account,vat_desc,vat_date],axis=1)
#df_all=pd.concat([bank_all,vat_all])
#df_all.to_excel("purchases_entry.xlsx")


purchases_debit=purchases_amount
purchases_credit=purchases_debit*0
purchases_account=purchases_credit+41
purchases_desc=vat_desc
purchases_all=pd.concat([purchases_debit,purchases_credit,purchases_account,purchases_desc,purchases_date],axis=1)

df_all=pd.concat([bank_all,vat_all,purchases_all])
df_all.to_excel("purchases_entry.xlsx")
