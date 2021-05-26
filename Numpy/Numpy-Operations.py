import numpy as np

#ARITHMETIC
arr = np.arange(0,11)
arr + arr
arr * arr
arr - arr
arr ** 3

arr / arr
# x/0 - It doesnt give you an error, it provides a warning
# nan = no object back

1/arr       #Also provides a warning. inf = infinite

#UNIVERSAL ARRAY FUNCTIONS
#https://numpy.org/doc/stable/reference/ufuncs.html
#https://numpy.org/doc/stable/reference/routines.math.html
#https://numpy.org/doc/stable/reference/routines.statistics.html

np.sqrt(arr)   #square root
np.exp(arr)    #exponential: (e^x) - Euler # 2.71
np.max(arr)    #Maximum = arr.max()
np.sin(arr)    #Trigonometric functions
np.log(arr)    #Logarithm
np.greater(arr,5)  #Comparison functions (returns boolean)

np.sum()       #Sum of items in the array
np.prod()
np.nansum()    #Sum of # items. Not # are = 0
np.nanprod()

np.median()
np.average()
np.mean()
np.std()
np.var()

#ALSO: Can run this functions with the variable
mat = np.arange(1,26).reshape(5,5)

mat.std()
mat.sum()
mat.sum(axis=0)   #Cumulative sum of every row
mat.sum(axis=1)   #Cumulative sum of every column
