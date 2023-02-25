# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 22:45:28 2023

@author: Iqraa
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <---- format of read csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#Wordking with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathemtical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = ProfitPerItem * NumberofItemsPurchased
CostPerTransaction = NumberofItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem


#CostPerTransaction Column Calculation

#CostPerTransaction = NumberofItemsPurchased * CostPerItem
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding a new column to a dataframe

data['ConstPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales -Cost

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['ConstPerTransaction']

#Markup = (Sales - Cost)/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['ConstPerTransaction'])/data['ConstPerTransaction']

#Rounding Markup
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#combining data fields

day = data['Day'].astype(str)
year = data['Year'].astype(str)

my_date = day+'-'+data['Month']+'-'+year
data['data'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3]  #first 3 rows
data.iloc[-5:]  #last 5 rows

#using split to split the client_keywords field
#new_var = columnn.str.split('sep', expand = True)
split_col = data['ClientKeywords'].str.split(',', expand=True)

#creating new columns for the split columns in Client Keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merg_df = pd.merg(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

#df = df.drop('columnname', axis =1)
data = data.drop('ClientKeywords', axis=1)
data = data.drop('Year', axis=1)
data = data.drop(['Month', 'Day'], axis=1)

#Export into CSV

data.to_csv('ValueInc_Clean.csv', index = False)















