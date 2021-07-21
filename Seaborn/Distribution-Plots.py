import seaborn as sns

#Seaborn comes with datasets. We need to call them:
tips = sns.load_dataset('tips')
print(tips.head())

#DISPLOT - Distribution univariant plot (only 1 variable) (HISTOGRAM)
sns.distplot(tips['total_bill']) #or:
sns.histplot(tips['total_bill'])
sns.distplot(tips['total_bill'],kde=False)         #Take off the kde (the line) (kernel density estimation)
sns.displot(tips["total_bill"],kde=False,bins=30)  #Change amount of bins

#JOINTPLOT (use 2 variables). Need to pass x, y, dataset (x,y columns)
sns.jointplot(x="total_bill",y="tip",data=tips)    #Show a scatter plot

#Kind (affects the view inside the plot). Parameters: scatter, reg, resid, kde, hex
sns.jointplot(x="total_bill",y="tip", data=tips, kind="hex") #hexagon view
sns.jointplot(x="total_bill",y="tip", data=tips, kind="reg") #regression
sns.jointplot(x="total_bill",y="tip", data=tips, kind="kde") #kernel density estimation

# PAIRPLOT - Do every possible combination between numerical columns in all the data frame
# Quick way to visualize data
# When x,y is the same, it will plot an histogram
# HUE - Pass a column name of a categorical variable. It will color the data points according hue column.
# PALETTE - Can change the color palette
sns.pairplot(tips, hue='sex',palette="coolwarm")

#RUGPLOT
# Plot a dash for every single point in the distribution (from the column that we choose)
# Like a flattened graph
sns.rugplot(tips['total_bill'])

#KDEPLOT
sns.kdeplot(tips['total_bill'])                 # Plot only the KDE without the bins
sns.kdeplot(x=tips['total_bill'],y=tips['tip']) # Plot the KDE OF 2 numerical variables