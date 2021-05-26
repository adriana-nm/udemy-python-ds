import numpy as np

arr = np.arange(0,11)
print(arr)

#BRACKET INDEXING
arr[1:5]

#BROADCASTING
arr[0:5] = 100

#BROADCASTING & SLICES (It modifies the original one)
#Slice in arrays it's only a view. NOT A COPY.
arr2 = np.arange(0,11)
slice_arr = arr2[0:6]
slice_arr[:] =99
print(arr2)

#COPY AN ARRAY (The copy won't modify the original one)
arr_copy =arr2.copy()
print(arr_copy)

#INDEXING A 2D ARRAY - arr_2d[row][col] or arr_2d[row,col]
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)         #all
print(arr_2d[0,:])      #row
print(arr_2d[1,0])    #individual element
print(arr_2d[:2,1:])  #shape
print(arr_2d[:,2])    #COLUMN (joined elem. in ONE ARRAY)
print(arr_2d[:,2:3])  #COLUMN (elements in column IN A MATRIX)

#Another option if I want the column in a colum array, use reshape:
arr_col = arr_2d[:,2]
print(arr_col.reshape(3,1))  #print in column (only a view)
print(arr_col)               #print a row array

# MATRIX ROWS ALL 0, 1, 2 ...
import numpy as np
arr2dz = np.zeros((10,10))
arr_length = arr2dz.shape[1]
for i in range (arr_length):
    arr2dz[i] = i
print(arr2dz)
arr2dz[[2,4,6,8]]           # Select certain rows only (index of row)

# MATRIX - EACH ROW 0,1,2,3,4,5,6,7,8,9
arr3dz = np.zeros((10,10))
arr_length = arr3dz.shape[1]
for i in range (arr_length):
    for n in range(0,10):
        arr3dz[i][n] = 0+n
print(arr3dz)

# BOOLEAN SELECTION
arr4 = np.arange(0,11)
arr4[arr4>2]

x = 5
arr4[arr4>=x]

#NEGATIVE SELECTION - Index start in 1 & from the end of the matrix
mat = np.arange(1,26).reshape(5,5)
print(mat[-1])                  #-1 is the last row in the matrix