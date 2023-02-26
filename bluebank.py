#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:01:19 2023

@author: hawarihamdan
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#nethod 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() ti get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#FICO Score




#applying for loops to loan date
#using first 10
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    
    except:
        cat = 'Unknown'
    ficocat.append(cat)
    
    ficocat = pd.Series(ficocat)
    
    loandata['fico.category'] = ficocat
    

    

    
#df.loc as conditional statements
#df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is meet'

#for interest rates, a new column is wanted, rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'
        

# #number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width =0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width=0.2)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'red')
plt.show()

#writing to csv
loandata.to_csv('loan_clean.csv', index=True)





