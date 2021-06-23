import numpy as np
import pandas as pd

ecom = pd.read_csv(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\04-Pandas-Exercises\Ecommerce_Purchases.csv")
print(ecom)

# Head of the DF
ecom.head()

#Type of data in each column
ecom.dtypes

# #Colums and Rows
ecom.shape
ecom.info()
ecom.columns

# Average Purchase Price
ecom['Purchase Price'].mean()

# Highest and lowest purchases prices
ecom['Purchase Price'].min()
ecom['Purchase Price'].max()

# #People has English 'en' as language of choice in the website
    #A)
    sum(ecom[ecom['Language']=='en'].value_counts())

    #B)
    ecom.groupby('Language').count().query('Language == "en"')


# #People has job title "Lawyer"
sum(ecom[ecom['Job']=='Lawyer'].value_counts())

# #People made purchase during AM / #People purchase PM
sum(ecom[ecom['AM or PM']=='AM'].value_counts())
sum(ecom[ecom['AM or PM']=='PM'].value_counts())

# 5 Most common Job Titles
    #A)
    ecom.value_counts('Job').head()
    ecom['Job'].value_counts().head()

    #B)
    ecom.groupby('Job').count().sort_values(by='Lot', axis= 0, ascending=False).head().filter(['Job','Lot'])

# Purchase price of transaction from Lot "90 WT"
ecom[ecom['Lot']== '90 WT']['Purchase Price']

# Email of person with Credit Card Number: 4926535242672853
ecom[ecom['Credit Card'] == 4926535242672853]['Email']

# #People has American Express as Credit Card Provider & purchase >95 USD

    #A) Returns all columns
    ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()

    #B) Return only the #
    #df.shape[0]
    ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].shape[0]
    #len(df.index)
    len(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].index)
    #df[df.columns[0]].count()
    ecom[ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].columns[0]].count()

# #People has Credit Card that expires in 2025
    #A) str.slice
    ecom['year'] = ecom['CC Exp Date'].str.slice(start=-2)
    ecom[ecom['year']=='25'].shape[0]


# 5 Most popular email providers/host

