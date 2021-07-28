#911 CALLS CAPSTONE PROJECT

# lat : String variable, Latitude
# lng: String variable, Longitude
# desc: String variable, Description of the Emergency Call
# zip: String variable, Zipcode
# title: String variable, Title
# timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# twp: String variable, Township
# addr: String variable, Address
# e: String variable, Dummy variable (always 1)

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = None

df = pd.read_csv(r'911.csv')
df.info()
df.head()

# What are the top 5 zipcodes for 911 calls?
df['zip'].value_counts().head()

# What are the top 5 townships (twp) for 911 calls?
df['twp'].value_counts().head()

#Take a look at the 'title' column, how many unique title codes are there?
df['title'].nunique()

#Use .apply() with lambda exp. & create column "Reason" (EMS, Fire, Traffic)
df['Reason']=df['title'].apply(lambda x: x.split(':')[0])
df.head()

#Most common Reason for a 911 call?
df['Reason'].value_counts().head()

#Create a countplot of 911 calls by Reason in Seaborn
sns.countplot(x='Reason', data=df)

#Time Information
#Data type of objects in timeStamp column?
type('timeStamp')

#Use pd.to_datetime to convert these strings into DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
type('timeStamp')
type(df['timeStamp'].iloc[0])

#Check the atribute hour from a DateTime object
time = df['timeStamp'].iloc[0]
time.hour

#Create 3 columns named Hour, Month, Dayofweek. Take info from DateTime object.
df['hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['month'] = df['timeStamp'].apply(lambda time: time.month)
df['dayofweek'] = df['timeStamp'].apply(lambda time: time.dayofweek)  #Here day of the week is numeric
df.head()

#Create column direct from DateTime with day of week in name
df['dayofweekready'] = df['timeStamp'].apply(lambda time: time.strftime('%a')) #Here day of week is in name

#Change dayofweek numeric to string name, using map function and a dictionary
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['dayofweek'] = df['dayofweek'].map(dmap)
df.head()

#Visualization
#Create a countplot of Day of Week. Bar showing different Reasons.
sns.countplot(x='dayofweek', hue='Reason', data=df, palette='viridis')
plt.legend(bbox_to_anchor=(1.02,1))

#Create a countplot of Months. Bar showing different Reasons.
sns.countplot(x='month',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)

#Create an object  where you group the DataFrame by the month column and use the count() method for aggregation
byMonth = df.groupby('month').count()
byMonth.head()

#Create a simple plot off of the dataframe indicating the count of calls per month
byMonth['lat'].plot()

#Use seaborn's lmplot() to create a linear fit on the number of calls per month
##If Month is index, the plot won't be able to acces to this data
##reset_index will take the data out into a column to use it in the plot
##byMonth.reset_index()
sns.lmplot(x='month',y='twp',data=byMonth.reset_index())

#Create a new column "Date" that contains the date from the timeStamp column. Apply .date() method.
##It shows a Timestamp object
t = df['timeStamp'].iloc[0]
print(t)

#This object allows to extract part of the data:
t.date()

#Group date column with count() aggregate & create plot of 911 calls
df['date'] = df['timeStamp'].apply(lambda t: t.date())
df.groupby('date').count()['lat'].plot()
plt.tight_layout()

#Recreate this plot with the reason traffic
df[df['Reason']=='Traffic'].groupby('date').count()['lat'].plot()
plt.title('Traffic')
plt.tight_layout()

#Recreate this plot with the reason Fire
df[df['Reason']=='Fire'].groupby('date').count()['lat'].plot()
plt.title('Fire')
plt.tight_layout()

#Recreate this plot with the reason EMS
df[df['Reason']=='EMS'].groupby('date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout()

#Another way to plot this with the axes format more clear:
import matplotlib.dates as mdates
# prepare data
ems = df[df['Reason'] == 'EMS'].groupby('date').count()
# create figure & axes
fig, ax = plt.subplots(figsize=(9, 4))
# plot data (axes=ax)
ems['twp'].plot(ax=ax)
# set number of major ticks
ax.xaxis.set_major_locator(plt.MaxNLocator(10))
ax.yaxis.set_major_locator(plt.MaxNLocator(4))
# set major ticks format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
# set xlim & ylim
plt.xlim(ems.index[0], ems.index[-1])
plt.ylim(50, 250)
plt.title('EMS')
plt.tight_layout()

#Create a Pivot table with calls info. Columns:hours & rows: days of the week
# aggcount = "count" will count the amount of data in the intersection
t = df['timeStamp'].iloc[0]
df['hour'] = df['timeStamp'].apply(lambda t: t.hour)
pt = df.pivot_table(index='dayofweek',columns='hour',values='lat',aggfunc="count")
pt

#Create a table like the previous one, with .unstack()
df.groupby(by=['dayofweek','hour']).count()['e'].unstack()

#Create Heatmap using the pivot table
sns.heatmap(pt,cmap='viridis')
plt.tight_layout()

#Change size of the Heatmap
#OPTION 1
import matplotlib.pyplot as plt
plt.figure(figsize=(12,4))
sns.heatmap(pt,cmap='viridis')

#Change size of the Heatmap
#OPTION 2
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12,6))
sns.heatmap(pt,cmap='viridis')

#Create a clustermap using this DataFrame
sns.clustermap(pt,cmap='viridis')

#Create a table with columns=months & rows= days of the week
pt2 = df.pivot_table(index='dayofweek', columns='month', values='e',aggfunc="count")
pt2

#Create a Heatmap with this new table
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12,6))
sns.heatmap(pt2,cmap='viridis')

#Create a Clustermap with this new table
sns.clustermap(pt2,cmap='viridis')
