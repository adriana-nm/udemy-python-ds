import matplotlib.pyplot as plt
#This import the library and turn interactive mode on.


#If you use Jupiter Notebook need the line. Allows to see the plot in the Jup. Not.
%matplotlib inline

#If you are not using Jup. Notebook, you need to end the following code at the end of the command.
plt.show()
#If you are in interactive mode it has no effect.


import numpy as np
x = np.linspace(0,5,11)
y = x ** 2
print(x)
print(y)


#FUNCTIONAL METHOD
plt.plot(x,y)  #You can add color adding a 3rd statement 'r-' (for red)
plt.xlabel('X Label')    #add an X Label
plt.ylabel('Y Label')    #add a Y Label
plt.title('Title')      #add a title

#Multiplots on the same canvas
plt.subplot(1,2,1)         # Number of rows, number of colums, plot number you are referring to.
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


#OBJECT ORIENTED METHOD
#OO #1 (More manual, 2 steps to create the axes)
fig = plt.figure()                      #Creates an object
axes = fig.add_axes([0.1,0.1,0.8,0.8])  #Create an axes and pass the position of the plot in a list.
                                        #The list has 4 arguments: left,bottom, width, height.
                                        #LEFT/BOTTOM: This means space from the border of the canvas to where it starts the plot.
                                        #Ex. space from left border to the left of the plot.
                                        #WIDTH/HEIGHT: Size of the graphic.
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')

#Multiplots in the same canvas
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.3,0.8])
axes2 = fig.add_axes([0.6,0.1,0.3,0.8]) # 2 Graphs are separated

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) # 1 Graph is inside the other one
axes1.plot(x,y)
axes1.set_title('LARGER PLOT')
axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')

#OO #2  (Create a subplot, only 1 step to create the axes)
    #fig,axes = allow to create the canvas and the axes together
    #nrows=number of plots in rows, ncols =number of plots in columns
fig,axes = plt.subplots(nrows=3, ncols=3) #Returns 9 plots
plt.tight_layout()          #Separates the plots, so they don't overlap

    # Axes is an array of matplotlib.axes, is a list of axes, so you can itirate throw the axes
    fig,axes = plt.subplots(nrows=1, ncols=4)
    for current_ax in axes:
        current_ax.plot(x,y)

    #Or we can index each axes
    fig,axes = plt.subplots(nrows=1,ncols=2)
    axes[0].plot(x,y)
    axes[0].set_title('First Plot')
    axes[1].plot(y,x)
    axes[1].set_title('Second Plot')



#FIGURE SIZE & DPI

#Size with OO#1 Method
fig = plt.figure(figsize=(4,2)) #Figsize is a tuple, with width & hight of figure in inches
                                #Optional (dpi=) dots/pixels per inch. If you dont complete it, it uses the default.

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

#Size with OO#2 Method
fig,axes = plt.subplots(figsize=(4,2))  #1 Plot
axes.plot(x,y)

fig,axes = plt.subplots(nrows=2, ncols=1, figsize= (5,2)) #More than 1 plot
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()


#SAVE A FIGURE
#You can save it in png, jpeg,ips, spg, pgf, pdf.
fig.savefig('my_picture.png')   #Create the name of the image (figure)
                                #You can specify the dpi (dpi = ...)


#ADD LEGENDS
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,x**2, label='X Squared') #For a legend, I need to create a label here.
ax.plot(x,x**3, label='X Cubed')   #For a legend, I need to create a label here.

ax.legend()     #It reference the label I create in each plot

    #If legend overlap the plot, then use loc= .There are codes for the positions, ex. best 0, upper right 1
    #Codes: https://matplotlib.org/stable/api/legend_api.html?highlight=legend#module-matplotlib.legend
    ax.legend(loc=0)
    #If non of the options are good, then you can specify a 2-tuple (x, y) places the corner of the legend specified by loc at x, y.
    ax.legend(loc=(0.1,0.1))

