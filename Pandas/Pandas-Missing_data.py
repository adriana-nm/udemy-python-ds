#If Pandas find a missing value will fill it with NULL or NaN value.
#To avoid it, use following methods

import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}  #Dictionary. np.nan is a missing value
df = pd.DataFrame(d)
print(df)

#DROP MISSING VALUES
df.dropna()         #Will drop all the ROWS with a missing value (1 or more)
df.dropna(axis=1)   #Will drop any COLUMNS with a missing value
                    #NOT PERMANENT (for permanent use inplace)
df.dropna(thresh=2) #If you have >2 Non NAN values (real values) it won't delete the row

#REPLACE THE MISSING VALUES
df.fillna(value=0)  #Fill all the NaN with a value I instruct
df['A'].fillna(value=df['A'].mean()) #Fill missing value in a column with the mean of the column

# Statistical methods to fill values! (depends on what type of data you are working with)

```
https://blog.usejournal.com/missing-data-its-types-and-statistical-methods-to-deal-with-it-5cf8b71a443f
https: // www.ncbi.nlm.nih.gov / pmc / articles / PMC3668100 /  #:~:text=Listwise%20deletion%20is%20the%20most,the%20estimation%20of%20the%20parameters.
https://ec.europa.eu/eurostat/cros/system/files/webinar_missdata_may23_0.pdf
https: // www4.stat.ncsu.edu / ~davidian / st790 / notes / chap1.pdf
chapter 1-7
```