import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,5,11)
y = x ** 2


#ADD A COLOR (color='')
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color='orange') #Use name of the color
ax.plot(x,y,color='#00FF00')  #Use RGB Hex code (#dddddd). Ex. lime

#LINE WIDTH (linewidth= or lw=)
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color='purple',linewidth=5) #Default linewidth=1. You can increase or reduce the line width.
ax.plot(x,y,color='purple',lw=5)        #You can also use lw=

#LINE TRANSPARENCY (alpha=)
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color='purple',linewidth=3, alpha=0.5) #Default=1. Reduce the alpha to increase transparency.

#LINE STYLE (Dashes, dot) (linestyle='' OR ls='')
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color='purple',linewidth=3, linestyle='--')     #2 Dash line
ax.plot(x,y,color='purple',linewidth=3, linestyle='-.')     #Dash & dot line
ax.plot(x,y,color='purple',linewidth=3, linestyle=':')      #Dot line
ax.plot(x,y,color='purple',linewidth=3, linestyle='-')      #Default. Plot a continuous line.
ax.plot(x,y,color='purple',linewidth=3, linestyle='--',drawstyle='steps') #It plots a stair

#MARKERS (marker='' , markersize= , markerfacecolor= , markeredgewidth= , markeredgecolor =)
#Used when you have few data points. Mark the points of your data.
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color='purple',lw=0.5, marker='1',markersize=8) #Type of Markers: o,+,*,1(represent >-)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color='black',lw=2, marker='o',markersize=10,
        markerfacecolor='orange',markeredgewidth=2,markeredgecolor='blue')

#PLOT RANGE (ax.set_xlim /  ax.set_ylim)
#Limit the axes in a range of certain values
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color='purple',lw=2, ls='--')
ax.set_xlim([0,1])          #Enter the range in X I want to show
ax.set_ylim([0,2])          #Enter the range in Y I want to show

#SPECIAL PLOT TYPES
#Barplots, histograms, scatter plot, other. Can be done in mpt, but better in Seaborn.
