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

df.loc[['A','B'],['W','Y']]  #Select a subset


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
df > 0     #Return a boolean data frame

booldf = df > 0   #Return values under the condition
df[booldf]

df[df>0]           #Return values under the condition (simplified)

df['W']>0          #Return boolean column

df[df['W']>0]      #!Return the data frame, with the rows that meet the condition (in column W)

df[df['W'>0]['X']] #Multiple selection in one step


# MULTIPLE CONDITIONAL SELECTION  (Do not use "AND" or "OR"! use & | )
df[(df['W']>0) & (df['Y']>1)]     #Each condition must be inside a parenthesis


# RESET INDEX (Index will be back to be numeric. Old index will become a column in the DF)
df.reset_index()    #Again, only temporal unless I use "inplace=True"

# SET A COLUMN AS INDEX
newind = 'CA NY WY OR CO'.split()
df['States'] = newind             #Create the column I want to be index

df.set_index('States')            #Set the column I want to be index
                                  #Beware! It will overwrite the previous index & "States" will become a row.
                                  #Again, add argument "inplace" to be definitive

