import numpy as np
import pandas as pd

#With the previous libraries it will look like matplotlib
#But if you import seaborn, it will look better IN JUP. NOT. (like a Seaborn plot)
import seaborn as sns

df1 = pd.read_csv(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\07-Pandas-Built-in-Data-Viz\df1")
print(df1.head())

df2 = pd.read_csv(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\07-Pandas-Built-in-Data-Viz\df2")
print(df2.head())

#Built in Functions

#1)You can call directly
df1['A'].hist()
df1['A'].hist(bins=30)          #You can add Matplotlib arguments (like bins)

#2)You can use "plot" and define the type of graph with "kind"
df1['A'].plot(kind='hist',bins=30)

#3)You can use "plot" and the graph you want
df1['A'].plot.hist(bins=50)
df2.plot.area(alpha=0.4)                        #Area graph of all the values. Alpha is the transparency.
df2.plot.bar()                                  #Bar graph
df2.plot.bar(stacked=True)                      #Stacked bar graph
df1.reset_index().plot.line(x='index',y='B')    #Line plot. Need to declare x and y.
                                                #If you put a column as an index, you need to use reset_index()
                                                #Otherwise just use the column in the x=''
df1.reset_index().plot.line(x='index',y='B',figsize=(12,3),lw=1)    #You can apply MPT arguments
df1.plot.scatter(x='A',y='B')                   #Scatter plot
df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm') #You can add a 3rd variable/data in the scatter plot in color(Black/White)
                                                    #Use c='column'. To change color use "cmap"
df1.plot.scatter(x='A', y='B',s=df1['C']*100)       #You can also add a 3rd variable/data by size
                                                    #s=number changes the Size of the points in the scatter plot
df2.plot.box()                                  #Boxplot. Will plot all the columns
df3[['A','B']].plot.box()                       #To plot only certain columns, need to pass a list with the columns

df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
df.plot.hexbin(x='a',y='b',gridsize=25)                 #Scatter plot with hexagonal bins (1 color) (For bivariate data(2var))
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='coolwarm') #Scatter plot with hex. bins (Full color)
df2['a'].plot.kde()                                     #KDE line plot
df2['a'].plot.density()                                 #KDE line plot

#Style of the functions
#Options of style: 'default','ggplot', 'fivethirtyeight', 'dark_background', 'bmh'
#More options: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('default')
df1['A'].hist(linewidth=1,ec='white')

#Take legend outside the plot
f = plt.figure()
df2.iloc[0:30].plot.area(alpha=0.4,ax=f.gca())          # .gca gets the current axes, creating one if needed.
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()