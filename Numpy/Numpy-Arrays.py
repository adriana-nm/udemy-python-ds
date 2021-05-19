import numpy as np

#CREATE ARRAY FROM A PYTHON LIST
my_list = [1,2,3]
print(np.array(my_list))

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_matrix))

#BUILT IN METHODS

#ARANGE
np.arange(25)
np.arange(1,11)    #Last digit, not inclusive
np.arange(0,11,2)

#ZEROS
np.zeros(3)
np.zeros((3,5))    #2d

#ONES
np.ones(3)
np.ones((3,5))     #2d

#LINSPACE (start, end (is inclusive), amount of elements)
np.linspace(0,20,40)

#EYE (identity matrix)
np.eye(4)      #2d

#RANDOM:

#RAND - Uniform Distribution (0-1)
np.random.rand(5)
np.random.rand(5,5)     #2d

#RANDN - Standard Normal Distribution
np.random.randn(3)
np.random.randn(3,4)    #2d

#RANDINT - Integers (low inclusive, high exclusive)
np.random.randint(1,200)     #returns only 1 value
np.random.randint(1,150,10)

#ARRAY IN A VARIABLE
ranarr = np.random.randint(0,50,10)
print(ranarr)

#RESHAPE (an array variable)(reshape in 2 dimension)
arr = np.arange(25)
print(arr.reshape(5,5))   #2d

arr = np.arange(25).reshape(5,5)   #All in one line of code
print(arr)

#MIN/MAX (of an array variable)
arr = np.random.randint(0,25,8)
print(arr)
print(arr.max())
print(arr.min())

#ARGMAX/ARGMIN (of an array variable) (return index position)
arr = np.random.randint(0,25,8)
print(arr)
print(arr.argmax())
print(arr.argmin())

#SHAPE (Attribute, NOT A METHOD) (return # elements)
arr = np.random.randint(0,25,8)
print(arr.shape)

print(arr.reshape(8,1))            # Reshape in 2 dimension
print(arr.reshape(8,1).shape[1])   # !! # of elements in each row (Allways shape[1])
print(arr)                         # Will show original w/ no change
newshape = arr.reshape(8,1)        # If I want the new shape, I got to create a new variable
print(newshape)

print(arr.reshape(1,8))            #Seems 1 row, but is 2d


#DTYPE
print(arr.dtype)