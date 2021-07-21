import numpy as np
import seaborn as sns

#CATEGORICAL PLOTS: Seeing distributions of cat. columns and reference eather with num. columns

#BARPLOT (x,y,data) (x categorical, y numerical)
sns.barplot(x="sex",y="total_bill",data=tips)   #Shows the average/mean per categorical bin

#Default method for BARPLOT is average
#To change it use estimator=  (ex. pass a method)
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)  #Ex. method st. deviation (Need NUMPY)

#COUNTPLOT
sns.countplot(x='sex',data=tips)                # Counts the number of ocurrences

#BOXPLOT
#It divides the data on quarters, so each separation is 25% of data (The dots are outliers)
sns.boxplot(x='day',y='total_bill',data=tips)
sns.boxplot(data=tips,palette='rainbow',orient='h')         #Graph all the dataframe (num. columns) with orient='h'
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')  #Hue allows to add another categorical value into the graph.

#VIOLINPLOT ( Related with the boxplot)
#Shows a distribution verticaly & in mirror
sns.violinplot(x='day',y='total_bill',data=tips)
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex')  #Hue allows to add another categorical value
sns.violinplot(x='day',y='total_bill',data=tips,hue="sex",split='True') #Show 2 variables in 1 violin (instead of a mirror)

#STRIPPLOT (Scatter plot with 1 categorical, 1 numerical)
sns.stripplot(x='day', y='total_bill', data=tips)
sns.stripplot(x='day',y='total_bill',data=tips,hue='sex')               #Add another categorical variable
sns.stripplot(x='day',y='total_bill',data=tips,hue='sex',dodge=True)    #split/dodge: Will divide the categorical values in 2 colums

# jitter =True Will spread a little the points so you can see the areas with >density
# jitter = False All points will be in 1 line. You cannot tell how many points are stack on top of each other
sns.stripplot(x='day', y='total_bill', data=tips, jitter=False)

#SWARMPLOT (Combination from stripplot and violinplot) (Do not use it for large dataset, does not scale well)
sns.swarmplot(x='day',y='total_bill',data=tips)

#SWARMPLOT + VIOLINPLOT (You can plot the violinplot and add the points from the Swarmplot)
sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')

#FACTORPLOT / CATPLOT (You can plot different graphs, changing "kind")
sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')
sns.catplot(x='day',y='total_bill',data=tips,kind='bar')
sns.catplot(x='day',y='total_bill',data=tips,kind='violin')