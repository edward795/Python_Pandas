import pandas as pd 
import numpy as np

#Empty Dataframe 
df=pd.DataFrame()
print(df)

#from Lists 
df=pd.DataFrame(['a','b','c','d']) 
print(df)


data=[["Alex",20],["alok",30]] 
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)

#from ndarrays 
arr=np.array([["Apple","orange","grapes"],[2,4,8]]) 
df=pd.DataFrame(arr) 
print(df)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

#list of dictionaries
d=[{"a":1,"b":2},{"c":3,"d":4,"e":4}] 
df=pd.DataFrame(d) 
print(df)

d=[{"a":1,"b":2},{"d":3,"e":4,"f":5}] 
df=pd.DataFrame(d,index=["first","second"],columns=["a","b","f"])
print(df)
df=pd.DataFrame(d,index=["first","second"],columns=["f"])
print(df)

#from Series
d={"one":pd.Series([1,2,3,4],index=["a","b","c","d"]),
    "two":pd.Series([1,2,3,4,5,6],index=["a","b","c","d","e","f"])}
df=pd.DataFrame(d)
print(df) 


#Accessing Data 

#column Selection 
print(df["one"])

#Manipulating Data

#Column Addition 
d={"one":pd.Series([1,2,3],index=["a","b","c"]),
  "two":pd.Series([1,2,3,4],index=["a","b","c","d"])}
df=pd.DataFrame(d)
print(df)

df["three"]=pd.Series([1,2],index=["a","b"])
print(df)

df["four"]=df["three"]+df["two"]
print(df)

#column deletion 
#using del 

del df["four"]
print(df)

df.pop("three")
print(df)

#Row Selection,Addition,Deletion

#Selection by Label
print(df.loc["a"])

#Selection by integer location
print(df.iloc[2])

#Slice Rows
print(df[:1])

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df.append(df2) 
print(df)

#Deletion of Rows
df.drop(0)
print(df)