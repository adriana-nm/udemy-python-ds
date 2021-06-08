#GROUP BY: Similar as in SQL

import pandas as pd

# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

df.groupby('Company') #Return an object (and where it's located)
byComp = df.groupby('Company')  #You can: 1) save it in a variable & apply methods there
                                # 2) apply the methods at the end

print(byComp.mean())            # 1)
df.groupby('Company').mean()    # 2)

df.groupby('Company').sum()     #Other methods (sum, st. dev, count)
df.groupby('Company').std()     #Numeric methods will omit strings
df.groupby('Company').count()   #Count will return the # of instances (numeric or string)

df.groupby('Company').max()
df.groupby('Company').min()
#Beware! Max/min will return the corresp. value in each colum (if it's a string will be alphabetical)
#The string and # value may not correspond or be correlated (only returns min, does not respect to who correspond that value)
df.groupby('Company').min('Sales')
#I can inform the column of the min, but it wont show the string column corresponding

# to get actual maximum and minimum sales by person
by_comp = df.groupby('Company')
print(by_comp.apply(lambda df: df.loc[df['Sales'].idxmax()]))
by_comp.apply(lambda df: df.loc[df['Sales'].idxmin()])

df.groupby('Company').sum().loc['FB'] #Select 1 value

df.groupby('Company').describe()            #Creates a statistical description (count, mean, std, min, quartiles, max)
df.groupby('Company').describe().transpose() #Inverts the column and the index
df.groupby('Company').describe().transpose()['FB']  #You can call a single column (company in this ex.)
