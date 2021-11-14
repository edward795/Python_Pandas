"""
A panel is a 3D container of data. The term Panel data is derived from econometrics and is partially responsible for the name pandas − pan(el)-da(ta)-s.

The names for the 3 axes are intended to give some semantic meaning to describing operations involving panel data. They are −

items − axis 0, each item corresponds to a DataFrame contained inside.

major_axis − axis 1, it is the index (rows) of each of the DataFrames.

minor_axis − axis 2, it is the columns of each of the DataFrames.

########################################################################################
Note:This Data Structure has been removed from pandas 0.25.0 verion onwards
#######################################################################################
"""

import numpy as np 
import pandas as pd 

arr=np.random.rand(2,4,5) 
p=pd.Panel(arr)
print(p)

"""
Output:

<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 5 (minor_axis)
Items axis: 0 to 1
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 4

"""

data={"item1":pd.DataFrame(np.random.rand(2,4)),
      "item2":pd.DataFrame(np.random.rand(4,3))}
p=pd.Panel(data) 
print(p)

#Selecting the Data from Panel

#Using Items

# creating an empty panel
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p['Item1'])


"""
            0          1          2
0    0.488224  -0.128637   0.930817
1    0.417497   0.896681   0.576657
2   -2.775266   0.571668   0.290082
3   -0.400538  -0.144234   1.110535

"""

#Using major_axis
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p.major_xs(1))

"""
      Item1       Item2
0   0.417497    0.748412
1   0.896681   -0.557322
2   0.576657       NaN

"""

#Using minor_axis
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p.minor_xs(1))

"""
       Item1       Item2
0   -0.128637   -1.047032
1    0.896681   -0.557322
2    0.571668    0.431953
3   -0.144234    1.302466

"""

