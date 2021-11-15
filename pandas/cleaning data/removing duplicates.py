"""
To discover duplicates, we can use the duplicated() method.

The duplicated() method returns a Boolean values for each row:
"""
import os 
import pandas as pd 
import numpy as np 

cwd=os.getcwd()
filename=os.path.join(cwd,'pandas','cleaning data','dirtydata.csv') 

df=pd.read_csv(filename)
print(df.duplicated())

""""
Removing Duplicates
To remove duplicates, use the drop_duplicates() method.
"""

print(df.drop_duplicates(inplace=True))

print(df)