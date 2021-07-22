import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())
iris['species'].unique()

#PAIRPLOT - Do every possible combination between numerical columns in all the data frame
sns.pairplot(iris)

#PAIRGRID - #Allow to customize the pairplot graphs
sns.PairGrid(iris)         #1)Create the grid empty without data
g = sns.PairGrid(iris)
g.map(plt.scatter)         #2)Plot the graphs


#2) The grid is simetrical, so I can control whats plotted on the diagonal, upper map & lower map
g = sns.PairGrid(iris)
g.map_diag(sns.distplot)  #or histplot #Plot the diagonal
g.map_upper(plt.scatter)  #Plot the upper right part of the grids
g.map_lower(sns.kdeplot)  #Plot the lower left part of the grids

#PAIRPLOT - simple version of PairGrid
sns.pairplot(iris,hue='species',palette='rainbow')

#FACETGRID - Grid 2 categorical variables
g = sns.FacetGrid(data=tips, col='time', row='smoker')  #Creates empty grid
g.map(sns.distplot,'total_bill')

#If you need more than 1 argument (ex. based on total_bill & tip):
#1) add the second argument in map line, 2) change the graph (ex. plt.scatter)
g = sns.FacetGrid(data=tips, col='time', row='smoker')  #Creates empty grid
g.map(plt.scatter,'total_bill','tip')