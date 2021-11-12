"""
What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

"""
import os

import pandas as pd
calories={
    "name":["Amal","Kiran","John"],
    "age":[22,25,21]
}

table=pd.DataFrame(calories) 
print(table)

"""
Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)
"""

print(table.loc[0])

print(table.loc[[0,1]])


"""
Named Indexes
With the index argument, you can name your own indexes.
"""

employees={
    "name":["rahul","john","karan"],
    "age":[21,24,20] 
}

df=pd.DataFrame(employees,index=["emp1","emp2","emp3"])
print(df)

"""
Locate Named Indexes
Use the named index in the loc attribute to return the specified row(s).
"""

print(df.loc["emp3"])

"""
Load Files Into a DataFrame
If your data sets are stored in a file, Pandas can load them into a DataFrame.
"""

pwd=os.getcwd() 
path=os.path.join(pwd,'pandas','data.csv')
df=pd.read_csv(path) 

print(df)