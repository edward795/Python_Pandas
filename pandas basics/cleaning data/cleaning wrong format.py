"""
Data of Wrong Format
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
"""
import os 
import pandas as pd 
import numpy as np 

cwd=os.getcwd()
filename=os.path.join(cwd,'pandas','cleaning data','dirtydata.csv') 

df=pd.read_csv(filename)
print(df)

#date column correction 

df["Date"]=pd.to_datetime(df["Date"])
print(df)

"""
  Removing Rows
The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.
"""

df.dropna(subset=['Date'],inplace=True)
print(df)