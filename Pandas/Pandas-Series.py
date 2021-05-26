# Series: similar to an array, but it can have axis labels
# Labels don't need to be #, it can be any object (value, text, function)
# Method: Series(data (point), index)
# In Series, a list and array works equal

import numpy as np
import pandas as pd

#CREATE A SERIES (from a list, numpy array or dictionary)
labels = ['a','b','c']
my_list= [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
pd.Series(list)

pd.Series(data=my_list)
pd.Series(data=my_list,index=labels)
pd.Series(my_list,labels)          #Same as before, shorter code
pd.Series(arr,labels)
pd.Series(d)

pd.Series(data=labels)       #dtype: object
pd.Series([sum,print,len])   #dtype: object

# USING AN INDEX (like a dictionary)
ser1 = pd.Series([1,2,3,4],index=['USA','Germany','Rusia','Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4],index=['USA','Germany','Italy','Japan'])
print(ser2)

ser1['Germany'] # Extract data from the series ['index']
ser1 + ser2     # It adds the values of the data (based on same index)
                # If index cannot sum, then NaN (Null value)
                # Beware! Values will be converted to FLOAT