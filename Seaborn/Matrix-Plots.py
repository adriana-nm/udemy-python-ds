import seaborn as sns

#Seaborn comes with datasets. We need to call them:
tips = sns.load_dataset('tips')
print(tips.head())

flights=sns.load_dataset('flights')
print(flights.head())

#HEATMAP
#Data must be in a matrix form (index name and column name match up with cell value, that indicates sthg valuable for both of those names)

tc = tips.corr()                    #1) Create a matrix (with a pivot table or correlation table) EX: CORR
sns.heatmap(tc)                     #2) Call heatmap
sns.heatmap(tc, annot=True)         #Annot= Shows the actual value of each cell
sns.heatmap(tc, annot=True, cmap='coolwarm')    #cmap= change the colors

fp = flights.pivot_table(index='month',columns='year',values='passengers') #1) Create a matrix (Ex.Pivot Table)
sns.heatmap(fp)                     #2) Call heatmap.
                                    #Cmap= color (Ex. magma) See more in Style&Color.
#If you want the heatmap to be separated you can > the width of the lines (linewidth) and set the color (linecolor)
sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)


#CLUSTER MAP (Usefull for machine learning)
#Cluster information to show columns and rows that are similar to each other
#The columns & rows won't be in order anymore
sns.clustermap(fp, cmap='coolwarm')
sns.clustermap(fp,cmap='coolwarm',standard_scale=1) #Standard scale. It normalizes the cluster, from 0-1