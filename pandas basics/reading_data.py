import os 
import pandas as pd 
path=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(path,'data.csv')

"""
Viewing the Data
One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top.
"""

df=pd.read_csv(filename)
print(filename)

print(df.head(2))

"""
There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom.
"""

print(df.tail())

"""
Info About the Data
The DataFrames object has a method called info(), that gives you more information about the data set.

"""

print(df.info())