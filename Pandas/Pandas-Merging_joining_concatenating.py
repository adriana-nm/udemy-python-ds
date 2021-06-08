import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


#CONCATENATION (Glues together DataFrames)

print(pd.concat([df1,df2,df3])) #axis=0, join the columns (if they are the same)
print(pd.concat([df1, df2, df3],axis=1))  #axis=1 doesn't join the columns. Missing data will be NaN.


#MERGING (Merge DataFrames using a Key column,similar to SQL)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right,how='inner',on="key"))

#MERGING W/ MULTIKEYS

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

#INNER (Merge only when both keys match, K0 K0 & K1 K0 (2 times))
# You can pass a list of keys
print(pd.merge(left,right,on=['key1','key2']))

#OUTER MERGE (Shows all the combination of keys that exist)(Missing data = NaN)
print(pd.merge(left,right, how='outer', on=['key1','key2']))

#RIGHT MERGE (Merge only the keys that are on the right table (2nd table))
print(pd.merge(left,right, how='right', on=['key1','key2']))

#LEFT MERGE (Merge only the keys that are on the left table (1st table))
print(pd.merge(left,right, how='left', on=['key1','key2']))


#JOINING
#Method to combine columns of 2 potentially differently-indexed DF into a single DF
#Similar to merge, except the KEYS are the INDEX.

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

print(left.join(right)) #Inner Join. Takes the index from left DF and completes the table with right DF

print(left.join(right, how='outer')) #Join both DF considering ALL the indexes
