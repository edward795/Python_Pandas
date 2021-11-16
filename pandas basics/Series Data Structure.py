import pandas as pd
 

"""
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
"""
arr=[1,2,3,4,5] 

x=pd.Series(arr)
print(x)

"""
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.
"""

print(x[0])
print(x[1])

"""
Create Labels
With the index argument, you can name your own labels.
"""

y=pd.Series(arr,index=['a','b','c','d','e']) 
print(y)

print(y['a'])
print(y['b'])

"""
Key/Value Objects as Series
You can also use a key/value object, like a dictionary, when creating a Series.
"""

dict={'a':'apple','b':'ballon','d':'dog'}
d=pd.Series(dict)
print(d)

"""
Note: The keys of the dictionary become the labels.

To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.N
"""

calories={"day1":420,"day2":380,"day3":390} 
var=pd.Series(calories,index=["day1","day2"]) 
print(var)

"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
"""

data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myVar=pd.DataFrame(data)
print(myVar)


