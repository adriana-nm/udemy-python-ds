import seaborn as sns

#Seaborn comes with datasets. We need to call them:
tips = sns.load_dataset('tips')
print(tips.head())


# LMPLOT
# Display linear models with seaborn
sns.lmplot(x='total_bill',y='tip',data=tips)
    *hue = "cat. column"    #It will color the diff. categories
    *palette = "color"

#Markers
# http://matplotlib.org/api/markers_api.html
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',
           markers=['o','v'],scatter_kws={'s':100})
    *markers=       #['form','form'] Change the form (it use the matplotlib markers symbols)
    *scatter_kws=   #{'s':100} Change the marker size. Need to pass a dictionary.

#Grid
#Separate the graph on 2 or + plots, based on 1 or + a categorical column
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')  #Add the cat.column with col and/or row
sns.lmplot(x="total_bill", y="tip",data=tips, row="sex", col="time")
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm') #Add hue to add more cat. info.

#Aspect and Size
#If size is too small, so you can use: "aspect" ratio (between height and width) & "height"
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,size=8)