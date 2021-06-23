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
    #A) idxmax (pandas method)
    sal.iloc[sal['TotalPayBenefits'].idxmax()]['EmployeeName']

    #B) argmax (numpy method)
    sal.iloc[sal['TotalPayBenefits'].argmax()]['EmployeeName']

    #C)
    sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']


#Name of lowest paid person (including benefits)
sal.iloc[sal['TotalPayBenefits'].idxmin()]['EmployeeName']

#Average(mean) BasePay of all employees per year? (2011-2014)?
    #A)
    sal.groupby('Year').mean()['BasePay']

    #B)
    sal.groupby('Year').mean('BasePay')['BasePay']

#How many unique job titles are there?
sal['JobTitle'].nunique()

#Top 5 most common jobs?
    # A)
    sal['JobTitle'].value_counts().head()
        # .value_counts  # ocurring elements in descending value, in the column

    # B)
    sal.groupby('JobTitle').count().sort_values(by='Id',axis=0,ascending=False,).iloc[0:5].filter(['JobTitle','Id'])
        # .count()        # ocurring elements in all colums in the GROUPED OBJECT. Here I take ID, because it's a unique number. So it returns # of IDs that had this JobTitle.
        # .sort_values()  sort the rows
        # .filter()       filter the columns I need

#How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)

    # A)
    sal.query('Year == 2013').groupby('JobTitle').count().query('Id == 1').shape[0]
        # sal.query('Year == 2013')     Filter rows in year 2013
        # .groupby('JobTitle')          Object group JobTitle
        # .count()                      # Rows of instances in JobTitle
        # .query('Id == 1')             Rows that has only 1 occurrence
        #.shape[0]                      # Rows

    # B)
    sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts()==1)

#How many people have the word Chief in their job title?

    # A)
    sal[sal['JobTitle'].str.contains('CHIEF', case=False)].shape[0]
        # .str.contains('CHIEF', case=False) Filter rows that contain those words
        #                                    case=False, not case sensitive
        # .shape[0]                          # Rows

    # B)
    def chief_string(title):
        if 'chief' in title.lower().split():
            return True
        else:
            return False

    sum(sal['JobTitle'].apply(lambda x: chief_string(x)))


#Is there a correlation between length of the Job Title string and Salary?
    # A)
    def countlet(x):
        count = 0
        for letter in x:
            count = count +1
        return count

    sal['TitleLen'] = sal['JobTitle'].apply(countlet)
    sal.filter(['TitleLen','TotalPayBenefits']).corr()
        #.apply   Runs a function

    # B)
    sal['TitleLen'] = sal['JobTitle'].str.len()
    sal.filter(['TitleLen','TotalPayBenefits']).corr()
        #.str   Transform it in string
        #.len   Method of string, returns lenght of charachters

    # C)
    sal['TitleLen'] = sal['JobTitle'].apply(len)
    sal.filter(['TitleLen', 'TotalPayBenefits']).corr()