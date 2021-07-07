import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)

#LOGARITHMIC SCALE (with set_yscale("log"))
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x, x ** 2,x, np.exp(x))
axes[0].set_title("Normal scale")
axes[0].set_xlim(0,5)
axes[0].set_ylim(0,160)
axes[1].plot(x, x ** 2, x, np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")
axes[1].set_xlim(0,5)
axes[1].set_ylim(0,1000)

#TICKS / SEPARATED SPACES ON AXES
# Set the spaces I want in the axes (with set_xticks + set_yticks)
# Set the labels of the spaces in the axes (with set_xticklabels + set_yticklabels)
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, x**2, x, x**3, lw=2)
ax.set_xlim(0,5)
ax.set_ylim(0,150)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)

yticks = [0, 50, 100, 150]
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18) #LaTeX formatted labels

#AXIS GRID (Turn on/off grid lines)
fig, axes = plt.subplots(1, 2, figsize=(10,3))

# default grid appearance
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

# custom grid appearance
axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)

#AXIS SPINES (lines noting the data area boundaries)
fig, ax = plt.subplots(figsize=(6,2))

ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('blue')

ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)

# turn off axis spine to the right
ax.spines['right'].set_color("none")
ax.yaxis.tick_left() # only ticks on the left side

#TWIN AXES (on the right & left of the plot)
fig, ax1 = plt.subplots()

ax1.plot(x, x ** 2, lw=2, color="blue")
ax1.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
for label in ax1.get_yticklabels():   #It colors every Tick in this axis
    label.set_color("blue")

ax2 = ax1.twinx()
ax2.plot(x, x ** 3, lw=2, color="red")
ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")

#AXES WHERE X & Y IS ZERO
fig, ax = plt.subplots()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))   # set position of y spine to y=0

xx = np.linspace(-0.75, 1., 100)
ax.plot(xx, xx**3)

#SCATTER GRAPH
fig, axes = plt.subplots(1, 1, figsize=(12,3))
axes.scatter(xx, xx + 0.25*np.random.randn(len(xx))) #If I have > 1 graph I put axes[n].scatter()
axes.set_title("scatter")

#STEP GRAPH
n = np.array([0,1,2,3,4,5])
fig, axes = plt.subplots(1, 1, figsize=(12,3))
axes.step(n, n**2, lw=2)
axes.set_title("step")

#BAR GRAPH
n = np.array([0,1,2,3,4,5])
fig, axes = plt.subplots(1, 1, figsize=(12,3))
axes.bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes.set_title("bar")

#FILL BETWEEN GRAPH
fig, axes = plt.subplots(1, 1, figsize=(12,3))
axes.fill_between(x, x**2, x**3, color="green", alpha=0.5);
axes.set_title("fill_between")
axes.set_xlim(0,5)
axes.set_ylim(0,140)

#TEXT ANNOTATION (Inside the graph)
# Need to use LaTex formatting
fig, ax = plt.subplots()
ax.plot(xx, xx**2, xx, xx**3)

ax.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
ax.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green")


#CREATE FIGURES OF MULTIPLE SUBPLOTS:

#A) WITH SUBPLOTS (Same shape)
fig, ax = plt.subplots(2, 3)
fig.tight_layout()


#B) WITH SUBPLOT2GRID (can adjust the shape)
#subplot2grid(shape, loc, rowspan=1, colspan=1)
#location like a data frame (row,column). Row 0 starts above, column 0 starts on the left.
#rowspan: Number of rows for the axis to span to the right.
#colspan: Number of columns for the axis to span downwards.
fig = plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
fig.tight_layout()

#C) WITH GRIDSPEC
# declare the height_ratio (height of every group of graphs)
# declare the width_ratio (width of every group of graphs)
import matplotlib.gridspec as gridspec
fig = plt.figure()
gs = gridspec.GridSpec(2, 3, height_ratios=[2, 1], width_ratios=[1, 2, 1])
for g in gs:
    ax = fig.add_subplot(g)
fig.tight_layout()

#ADD AXES TO THE MULTIPLE SUBPLOTS
fig, ax = plt.subplots()            #Create the figure
ax.plot(xx, xx**2, xx, xx**3)       #Plot it
fig.tight_layout()

# inset (=subplot inside) [1) create new ax inside), 2) plot it, 3) title]
inset_ax = fig.add_axes([0.2, 0.55, 0.35, 0.35]) # X, Y, width, height
inset_ax.plot(xx, xx**2, xx, xx**3)
inset_ax.set_title('zoom near origin')

# set axis range (limits of the inset)
inset_ax.set_xlim(-.2, .2)
inset_ax.set_ylim(-.005, .01)

# set axis tick locations (axis of the inset)
inset_ax.set_yticks([0, 0.005, 0.01])
inset_ax.set_xticks([-0.1,0,.1])



#SCIENTIFIC NOTATION (When you have larger numbers on axes)
# fig, ax = plt.subplots(1,1)
# ax.plot(x,x**2,x,np.exp(x))
# ax.set_title('Scientific Notation')
#
# ax.set_ysticks([0,50,100,150])
#
# from matplotlib import ticker
# formatter = ticker.ScalarFormatter(useMathText=True)
# formatter.set_scientific(True)
# formatter.set_powerlimits((-1,1))
# ax.yaxis.set_major_formatter(formatter)


