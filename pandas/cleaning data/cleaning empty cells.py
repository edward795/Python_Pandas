"""
Empty Cells
Empty cells can potentially give you a wrong result when you analyze data.
"""

import os 
import pandas as pd 


path=os.getcwd()
filename=os.path.join(path,'pandas','cleaning data','dirtydata.csv')
print(filename)

data=pd.read_csv(filename)
new_data=data.dropna()
print(new_data)

"""
Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

If you want to change the original DataFrame, use the inplace = True argument:

"""
print(data)
data.dropna(inplace=True)
print(data)

"""
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value
"""

df=pd.read_csv(filename) 
df.fillna(1234,inplace=True) 
print(df)

"""
Replace Only For a Specified Columns
The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame:
"""

df["Date"].fillna('2021/01/01',inplace=True) 
print(df)


"""
Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
"""

d=pd.read_csv(filename)
#mean
m=d["Calories"].mean()
d.fillna(m,inplace=True) 

#meidan
me=d["Pulse"].median()
d.fillna(me,inplace=True)

#mode
mo=d["Maxpulse"].mode()[0] 
d.fillna(me,inplace=True)
