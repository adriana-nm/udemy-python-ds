# Working with Jupiter: Make sure the file location of the examples are in the same location as the Jupiter notebook
# To see location of Jup. Not. put: pwd ->Returns the file location

import numpy as np
import pandas as pd

#CSV

#Read a file & see it as a DF
pd.read_csv(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\03-Python-for-Data-Analysis-Pandas\example")

#Read and create another file (to write on it)
df = pd.read_csv(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\03-Python-for-Data-Analysis-Pandas\example")
df.to_csv('My_output', index=False)     #Index=True - The index will be a colum in the new DF. If I put False I avoid this problem.
print(pd.read_csv('My_output'))

#EXCEL
#Pandas can only import data. Won't import formulas, images, macros.
#Using pd.read_excel may cause Pandas to crash
#Panda takes each sheet as a DF. At the moment of read neet to introduce the sheet name.
#2020 Updates in Anaconda: Use the excel extension + sheet_name='Sheet1', index_col=0, engine="openpyxl"

pd.read_excel(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\03-Python-for-Data-Analysis-Pandas\Excel_Sample.xlsx", sheet_name='Sheet1', index_col=0, engine="openpyxl")

df.to_excel('Excel_Sample2.xlsx', sheet_name="NewSheet")
???DE DONDE TOMA LA INFO SI NO LO APLIQUE A NINGUNA VARIABLE NI HANDEL
?? SOLO DE LA MEMORIA

#HTML
#Reads data of a table, but it doesn't convert it in a DF. It read's it as a LIST. (You can check type())

data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
type(data)
data[0].head()      #Usually en position 0 is all the information we need.
                    # We check it with head() that show the first results.
