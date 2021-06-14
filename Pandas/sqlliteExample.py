#SQL - (SQL LITE)


import pandas as pd
df = pd.read_csv(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\03-Python-for-Data-Analysis-Pandas\example")

# Driver is a library to connect with specific DB's
import sqlite3

# Connection object is your connection to the database,
# close that when you're done talking to the database all together.
con = sqlite3.connect(':memory:')

# Another option is a DB in a file system
# con = sqlite3.connect('db_in_file.db')

#Paste the info of a DF named df to the DB
df.to_sql('data', con)

# Cursor object is an iterator over a result set from a query.
# Close those when you're done with that result set.
cur = con.cursor()

# ResultSet is the result of the select query.
resultSet = cur.execute("select b, c from data order by c desc")

for row in resultSet:
    print(row)