import numpy as np
import pandas as pd

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype='string')

s.str.lower()
s.str.upper()
s.str.len()     #letters (NAN will return NA)

idx = pd.Index([" jack", "jill ", " jesse ", "frank"])

idx.str.strip()     #Delete spaces on the right/left
idx.str.lstrip()    #Delete spaces on the left
idx.str.rstrip()    #Delete spaces on the right

#CLEANING SPACES IN A COLUMN (Need to assign the new columns to the )
df = pd.DataFrame(np.random.randn(3, 2), columns=[" Column A ", " Column B "], index=range(3))
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
print(df)


#CONVERT DATA INTO STRING
t = pd.Series(["a", 2, np.nan], dtype="string") #When you create the series

s1 = pd.Series([1, 2, np.nan], dtype="Int64") #From an existing series
s2 = s1.astype("string")
type(s2[0])


#REMOVE UNWANTED DATA IN THE COLUMN
ndf = pd.DataFrame({'time':['09:00', '10:00', '11:00', '12:00', '13:00'],'result':['+52A', '+62B', '+44a', '+30b', '-110a']})
print(ndf)

    # A) WITH .str.replace - (Specify the substring/pattern to match)
    ndf['result'] = ndf['result'].str.replace(r'\D','')
    print(ndf)
    #permanent modification

    # need to convert it to an integer: series.astype()
    ndf['result'] = ndf['result'].str.replace(r'\D','').astype(int)
    print(ndf)
    ndf.dtypes

    # if you don't want to modify df in-place: DataFrame.assign
    df2 = ndf.assign(result=ndf['result'].str.replace(r'\D',''))
    print(ndf)
    #ndf unchanged
    print(df2)

    # B) WITH .str.extract
    ndf['result'] = ndf['result'].str.extract(r'(\d+)') #, expand=...)
    print(ndf)
    #expand=True, return a DataFrame, expand=False, return a Series

    # C) WITH .str.split and .str.get (if they all follow a consistent structure)
    ndf['result'] = ndf['result'].str.split(r'\D').str.get(1)
    print(ndf)


#EXTRACT SPECIFIC DATA IN THE COLUMN
mdf = pd.DataFrame({'mail':['sergiourt@hotmail.com', 'sergiogutierrez@gmail.com', 'rodriguezjj@hotmail.com', 'marcostz@gmail.com', 'perezrr@yahoo.com'],'hour':['09:14', '10:15', '16:44', '12:30', '13:25']})
print(mdf)

    # A) WITH .str.split + .str.get
    mdf['host'] = mdf['mail'].str.split('@').str.get(1)
    print(mdf)

    # B) WITH .str.findall  *Regex (not mandatory to be inside a parenthesis)
    mdf['host'] = mdf['mail'].str.findall(r'@\S+').astype(str).str.replace('@','')  #Regex find and extract @. Use other methods to clean the @
    print(mdf)

    mdf['host'] = mdf['mail'].str.findall(r'@(\S+)')    #Regex find @ but it doesn't extract it
    print(mdf)

    # C) WITH .str.extract * Regex inside a parenthesis (need a capture group)
    mdf['host'] = mdf['mail'].str.extract(r'(@\S+)', expand=False).astype(str).str.replace('@','')    #Regex find and extract @. Use other methods to clean the @
    print(mdf)

    mdf['host'] = mdf['mail'].str.extract(r'@(\S+)')    #Regex find @ but it doesn't extract it
    print(mdf)