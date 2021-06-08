# np.random.seed - You will have the same random numbers
# Column/rows are both series
# Data Frame = Group of series that share an index

import numpy as np
import pandas as pd

# CREATE A DATA FRAME
from numpy.random import randn  #Write to avoid writing the full method in the creation of the serie
np.random.seed(101)     #Use seed to obtain the same # everytime. Used for test.

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
# pd.DataFrame(shape,rows,columns)
print(df)

# EXTRACT/SELECT SET DATA
df['W']        #Extract only 1 column

df[['W','Z']]  #Extract >1 column

df.W
# You can use df.nameofcolumn but it might overwrite a method of df. Avoid it.

df.loc['C']    #Select only 1 row, based on the name. Returns a series
df.iloc[2]     #Select the row based on the # index. Same return.

#EXTRACT/SELECT SUBSETS OF DATA
df.loc['B','Y']              #Select only 1 data

df.loc[['A','B'],['W','Y']]  #Select a subset [[rows],[columns]]


# CREATE A NEW COLUMN
df['new'] = df['W']+df['Y']
print(df)

# DELETE A COLUMN
df.drop('new',axis=1)
    #Will show it without the column, but it's only temporal. It doesnt affect the dataframe.
    #Need to declare axis, otherwise axis=0
    #Axis=0 it will search 'new' in rows, not columns

df.drop('new',axis=1,inplace=True)
print(df)
    #inplace - Makes the delete permanent.

# DELETE A ROW
df.drop('E')  #Not need to show axis, because default is 0
#df.drop('E',axis=0,inplace=True)  #Delete it permanently

# SHAPE
df.shape   #Retur the shape in a tuple (rows, colums)

# CONDITIONAL SELECTION
df > 0     #Return a BOOLEAN data frame

booldf = df > 0   #Return values under the condition
df[booldf]

df[df>0]           #Return VALUE under the condition (simplified)

df['W']>0          #Return BOOLEAN column

df[df['W']>0]      #!Return the data frame VALUES, with the rows that meet the condition (in column W)

df[df['W']>0]['Y'] #Multiple selection in one step


# MULTIPLE CONDITIONAL SELECTION  (Do not use "AND" or "OR"! use & | )
df[(df['W']>0) & (df['Y']>1)]     #Each condition must be inside a parenthesis


# RESET INDEX (Index will be back to be numeric. Old index will become a column in the DF)
df.reset_index()    #Again, only temporal unless I use "inplace=True"

# SET A COLUMN AS INDEX
newind = 'CA NY WY OR CO'.split()
df['States'] = newind             #Create the column I want to be index
#print(df)

df.set_index('States')            #Set the column I want to be index
                                  #Beware! It will overwrite the previous index & "States" will become a row.
                                  #Again, add argument "inplace" to be definitive

#MULTILEVEL INDEX OR INDEX HIERARCHY

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))           #Method, take 2 list & make a tuple joining 1 & 1 from each list.
hier_index = pd.MultiIndex.from_tuples(hier_index) #Function of pandas to make a multilevel index from tuples

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
#print(df)

df.loc['G1'].loc[1]     #Grab first outside index, then the inside
                        #Beware! Numeric index go without ''

df.index.names          #See if the indexes have names (object type: "none")

df.index.names = ['Groups','Num']  #Name each index
#print(df)

df.loc['G2'].loc[2]['B']  #Extract 1 data from the DF

#xs funtion: cross-section - To select >1 index at the same time
df.xs(1, level='Num')   #First name the index, second name the index column name
                        #Returns both rows under subindex 1
