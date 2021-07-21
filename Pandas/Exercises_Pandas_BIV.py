import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv(r"C:\Users\adri_\Desktop\Data Science\UDEMY - Python for Data Science and ML Bootcamp\Refactored_Py_DS_ML_Bootcamp-master\07-Pandas-Built-in-Data-Viz\df3")
print(df3.head())

# 1)Make a scatter plot of b vs a. Color red, big size, figure size big rectangle.
df3.plot.scatter(x='a',y='b', s=50, color='red',lw=1,ec='black',figsize=(11,3))

# 2)Create a histogram of the 'a' column
df3['a'].plot.hist(bins=10,ec='black')

# 3)Style the plot with 'ggplot', add more bins, lighter colors.
plt.style.use('ggplot')
df3['a'].plot.hist(bins=25,ec='white',alpha=0.5)

# 4)Create a boxplot comparing ONLY a & b columns
df3[['a','b']].plot.box()

# 5)Create a kde plot of the 'd' column
df3['d'].plot.kde(alpha=0.7)

# 6)Edit the kde plot: incerase linewidth and make a linestyle dashed
df3['d'].plot.kde(linestyle='--',lw=5)

# 7)Create an area plot of all the columns for just the rows up to 30
df3n = df3.iloc[:31,]
df3n.plot.area(alpha=0.5)

# 8)Take the legend out of the plot
f = plt.figure()
df3.iloc[0:30].plot.area(alpha=0.4,ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()