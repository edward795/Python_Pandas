import pandas as pd
import numpy as np

#empty series
s=pd.Series() 
print(s)

#Create a Series from ndarray
arr=np.array([23,45,67,89])
s=pd.Series(arr) 
print(s)

#giving indexes 
s=pd.Series(arr,index=[101,102,103,104])
print(s)

#from dictionaries  keys-->index 
d={'a':1,'b':2,'c':3,'d':4} 
s=pd.Series(d) 
print(s)

#giving custom indexes 
d={'a':1.,'b':2.}
s=pd.Series(d,index=[100,101,102,103])
print(s)


"""
Accessing Data from Series with Position
"""

arr=np.array([10,20,30,40,50,60,70,80,90.100])
s=pd.Series(arr)
print(s[0])

print(s[:3])

print(s[-3:])

"""
Retrieve Data Using Label (Index)
"""

s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e']) 
print(s)

print(s['a']) 

print(s[['a','b','c']])

print(s['f'])