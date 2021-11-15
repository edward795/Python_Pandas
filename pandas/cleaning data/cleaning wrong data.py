import os 
import pandas as pd 
import numpy as np 

cwd=os.getcwd()
filename=os.path.join(cwd,'pandas','cleaning data','dirtydata.csv') 
df=pd.read_csv(filename)


"""
Replacing Values
One way to fix wrong values is to replace them with something else.

In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
"""
print(df)
df.loc[7,'Duration']=45
print(df)


for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i,"Duration"]=120
print(df)

"""
Removing Rows
Another way of handling wrong data is to remove the rows that contains wrong data.

This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
"""

for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.drop(i,inplace=True)