"""
Read CSV Files
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

Tip: use to_string() to print the entire DataFrame.

By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows:

"""

import pandas as pd 
import os 

pwd=os.getcwd() 
path=os.path.join(pwd,'pandas','data.csv')

df=pd.read_csv(path) 
print(df)

print(df.to_string())

filename=os.path.join(pwd,'pandas','data.xlsx') 
df=pd.ExcelFile(filename)
print(df)

df=pd.read_excel(filename,sheet_name="Sheet1")
print(df.to_string())