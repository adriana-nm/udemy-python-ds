# MySql DB Engine
import mysql.connector

## These data are called connection string
## (IP, PORT, Credentials, databaseName)

con = mysql.connector.connect(
  host="localhost", # 127.0.0.1
  user="root",
  password="admin"
)

#Object that represents the result of a query
cur1 = con.cursor()
#To make more than 1 query, create more than 1 cursor
cur2 = con.cursor()

#Create an object with the query results
cur1.execute("SELECT * FROM prueba.new_table")

for row in cur1:
    print(row)

#Second query
cur2.execute("SELECT name FROM prueba.new_table LIMIT 2")
for row in cur2:
    print(row)