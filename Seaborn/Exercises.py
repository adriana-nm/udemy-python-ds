#TITANIC EXERCISE

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
titanic.head()

#1)Make a scatter plot with fare and age
sns.jointplot(x='fare',y='age',data=titanic)

#2)Bar graph of fare
sns.displot(titanic['fare'],kde=False,bins=30,color='red',alpha=0.5)

#3)Box plot of class & age
sns.boxplot(x='class',y='age',data=titanic, palette='rainbow')

#4)Swarmplot of class & age
sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')

#5)Countplot of sex category
sns.countplot(x='sex',data=titanic)

#6)Heatmap (make a correlation between variables)
g = titanic.corr()
sns.heatmap(g,cmap='coolwarm')

#7)2 Barplot of age, divided by sex
g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')