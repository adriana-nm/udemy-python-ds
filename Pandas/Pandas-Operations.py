
import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})

print(df.head())    #Function head: You get the first n rows (default n=5)

#MAIN METHODS TO FIND UNIQUE VALUES

df['col2'].unique() #Unique: Return array of unique values

len(df['col2'].unique())
df['col2'].nunique()    #Nunique: # of unique values

df['col2'].value_counts()   #Value_counts: How many times each unique value appears

#SELECTING DATA

df[(df['col1']>2) & (df['col2']==444)]

#APPLY METHOD (Allows to apply a method to a column)
#useful with lambda expressions

def times2(x):                  #Create a method
    return x*2

print(df['col1'].apply(times2)) #Use Apply to pass a method
print(df['col3'].apply(len))
print(df['col2'].apply(lambda x: x*2))  #Use Apply wits a lambda expression

#REMOVING COLUMNS
df.drop('col1',axis=1)  #To be permanent: inplace=True

#COLUMNS INDEX NAMES
df.columns   #Atribute

#INDEX NAMES
df.index     # Where index starts, where it ends

#SORTING/ORDERING A DF
df.sort_values('col2')  #It orders the DF according what I introduce in the ()

#NULLS
df.isnull()     #Result: Boolean DF. If data is null=TRUE, if data is not null = FALSE

#PIVOT TABLES

data = ({'A':['foo','foo','foo','bar','bar','bar'],
         'B':['one','one','two','two','one','one'],
         'C':['x','y','x','y','x','y'],
         'D': [1,3,2,5,4,1]})

df2 = pd.DataFrame(data)
print(df2)

df2.pivot_table(values='D',index=['A','B'],columns='C')  #Must indicate the values, index & colums