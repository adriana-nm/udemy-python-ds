import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

DISTRIBUTION PLOTS

-distplot: shows the distribution of a univariate set of observations.
-jointplot: allows you to basically match up two distplots for bivariate data.
-pairplot: will plot pairwise relationships across an entire dataframe (for the numerical columns) and supports a color hue argument (for categorical columns).
-rugplot: they just draw a dash mark for every point on a univariate distribution.
-kdeplot:  Kernel Density Estimation. KDE plots replace every single observation with a Gaussian (Normal) distribution centered around that value

sns.displot(dataset['num. column'],kde=False, bins=30)         #1var. Histogram
    *Old = distplot, New = displot, histplot
sns.jointplot(x='num. column',y='num. column',data=dataset, kind='') #2var. Scatter plot
    *kind -> hex(hexagon view), reg(regression view), kde(kernel dens. estimation)
sns.pairplot(dataset, hue='column',palette='color palet')      #Graph all combinations num. var.
    *hue -> Categorical column
    *same var. hist., diff. var. scatter plot
sns.rugplot(dataset['num. column'])
sns.kdeplot(dataset['num. column'])                            #kde for 1 num. var. (Dist.)
sns.kdeplot(x=tips['num. column'],y=tips['num. column'])       #kde for 2 num. var.

CATEGORICAL PLOTS

-factorplot
-stripplot: draw a scatterplot where one variable is categorical. It is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.
-swarmplot: similar to stripplot(), but the points are adjusted (only along the categorical axis) so that they don’t overlap. This gives a better representation of the distribution of values.
Are used to shown the distribution of categorical data:
-boxplot: distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution.
-violinplot:  shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a kernel density estimation of the underlying distribution.
Allow you to get aggregate data off a categorical feature in your data:
-barplot: is a general plot that allows you to aggregate the categorical data based off some function (default mean)
-countplot:same as barplot except the estimator is explicitly counting the number of occurrences

sns.barplot(x="cat. column",y="num. column",data=dataset)      #Barplot cat. var.
    *Optional add: estimator (barplot graph average, but with estimator you can use other operations)(converts a vector to scalar)
    *Ex. estimator=np.std  (need to: import numpy as np)
sns.countplot(x='cat. column', data=dataset)                   #Count # ocurrences in cat. var.
sns.boxplot(x='cat. column.',y='num. column.',data=dataset)    #Boxplot of cat/num var.
    *Optional: hue='cat. column'                               #It divides the boxplot with cat. column
    *orient='h'                                                #Will plot all num. columns with a boxplot graph
sns.violinplot(x='cat. columnn',y='num. column',data=dataset)  #Violin graph cat/num var.
    *Optional: hue='cat. column'                               #It shows several violins for each cat. option
    *Optional: split=True                                      #It shows both cat. var in 1 violin
sns.stripplot(x='cat. column', y='num. column', data=dataset)  #Scatter plot of 1 cat. + 1 num. column
    *Optional: hue='cat. column'                               #Will paint the diff. categories
    *Optional: dodge=True                                      #split/dodge Will separate both painted categories
sns.swarmplot(x='cat. column',y='num. column',data=dataset)    #Data points (Stripplot) in shape of violin(violinplot)

sns.violinplot(x='cat. column',y='num. column',data=dataset)               # 1)Violinplot
sns.swarmplot(x='cat. column',y='num. column',data=dataset, color='black') # 2)Put data points on top

sns.factorplot(x='cat. column',y='num. column',data=dataset,kind='type of graph') #Creates any graph. Only change kind.
    * Kind: This will define the type of graph (point, bar, count, box, violin, strip)
sns.catplot(x='cat. column',y='num. column',data=dataset,kind='type of graph')    #Catplot=Factorplot


MATRIX PLOTS

*Heatmap
variable = dataset.corr()               # 1) Option 1: Creates a Matrix with correlation
                                        # 1) Option 2: Creates a Matrix with pivot table
variable = dataset.pivot_table(index='cat. column',columns='cat. column',values='num. column')
sns.heatmap(variable)                   # 2) Heatmap
    *annot: =True wil show the value of the heatmap
    *cmap: ='Color combination' (coolwarm, magma...)
    *linecolors: ='color' Show the lines between the grid
    *linewidths: =#  Stablish the width of the line separating the grid

*Cluster map
sns.clustermap(variable)                # Join information on a cluster. Rows&columns not in order anymore.
    *cmap: ='Color combination' (coolwarm, magma...)
    *standard_scale=1                   #Normalize the cluster, from 0 to 1

GRIDS

*PairGrid
variable = sns.PairGrid(dataset)        # Creates empty graphic grid with combination of num. colums of the dataset
variable.map(plt.scatter)               # Graph scatter plot in all the grid (in all the combinations). It's simetrical.

Grid is simetrical, same info upper right & lower left. I can graph every part differently:
variable.map_diag(sns.distplot)         (or Hisplot) # Graph a dist. plot in the diagonal
variable.map_upper(plt.scatter)         # Graph a scatter plot in the upper right part of the grid
variable.map_lower(sns.kdeplot)         # Graph a kde plot in the lower left part of the grid

*Pairplot                               #Simple version of PairGrid
sns.pairplot(variable)
    *hue: ='cat. variable' It will separate in color the diff. categories

*Facetgrid                               #create grids of plots based off of a feature. (Grid 2 categorical variables)
                                         # 1) Creates an empty grid
variable = sns.FacetGrid(data=dataset, col='cat. column', row='cat. column)   #If you need you can only declare the row
variable.map(sns.distplot,'num. column') # 2) Graph a dist. plot on the grid
    * 2 num. columns: variable.map(plt.scatter,'num. column','num.column')
    * If you use sns.distplot it will plot a distribution. If you use plt.hist, a histogram.

REGRESSION

sns.lmplot(x='num. column',y='num. column', data=dataset)  #Graph the linear model (the regression)
    *hue: ='cat. column'        Will color the diff. categories in the plot
    *markers: =['o','v']        Will change the markers form (use matplotlib markers symbols)
    *scatter_kws: ={'s':100}    Will change the size of the marker
    *col: ='cat. column'        Will create 2 diff. graphs (if cat. column has 2 options)
    *row: ='cat. column'        Will create another 2 graphs (if cat. column has 2 options). Allows to put > info.
    *aspect: = #between 0-1(ratio between height & width) Will change the aspect of the grid
    *height: #                  Will change the height of the grid

STYLE & COLOR

sns.set_style('ticks')                      #1) Set the style (of the background)
                                            #1.1) Styles: dargrid, whitegrid, dark, white, ticks
sns.countplot(x='cat. column',data=dataset) #2) Create the plot (ex.)

sns.despine(left=True,bottom=True)          #Delete borders with ticks (rigth & up are True default)
plt.figure(figsize=(12,3))                  #Change the size to a grid of 12x3
sns.set_context('context par.')             #Change size according what context you need the graph for
                                            #Context parameters: paper, notebook, talk, poster (big visual)
    *font_scale: =# Will change the size of the font in the plot

When you graph a type of plot:
*palette: will change the color of graph.
(Matplotlib colormap: plasma, inferno, magma, viridis, seismic, coolwarm,spectral, more)
(https://matplotlib.org/stable/tutorials/colors/colormaps.html)