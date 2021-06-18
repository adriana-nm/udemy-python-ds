import pandas as pd

#NOTE: SETTING OPTION TO SHOW ALL COLUMNS WITH HEAD METHOD (ONLY USE ONCE)
pd.options.display.max_columns = None


#Read file salaries.csv
sal = pd.read_csv(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\04-Pandas-Exercises\Salaries.csv")

#Check head of the DF
print(sal.head())

#Print colums of the table
print(sal.columns.tolist())

#Use info method to see how many entries the DF have
sal.info()

#Average BasePay
sal['BasePay'].mean()

#Highest amount of OvertimePay
sal['OvertimePay'].max()

#Job title of JOSEPH DRISCOLL
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']

#How much does JOSEPH DRISCOLL make
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

#Name of highest paid person (including benefits)
sal.iloc[sal['TotalPayBenefits'].idxmax()]['EmployeeName']

#Name of lowest paid person (including benefits)
sal.iloc[sal['TotalPayBenefits'].idxmin()]['EmployeeName']

#Average(mean) BasePay of all employees per year? (2011-2014)?
sal.groupby('Year').mean('BasePay')['BasePay']

#How many unique job titles are there?
sal['JobTitle'].nunique()

#Top 5 most common jobs?
sal.groupby('JobTitle').count().sort_values(by='Id',axis=0,ascending=False,).iloc[0:5].filter(['JobTitle','Id'])

#How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
sal.query('Year == 2013').groupby('JobTitle').count().query('Id == 1').count


#How many people have the word Chief in their job title?


#Is there a correlation between length of the Job Title string and Salary?

