import seaborn as sns
import matplotlib as plt

#BACKGROUND STYLE
#You can set the style of the background with "set_style"
# darkgrid, whitegrid, dark, white, ticks
sns.set_style('ticks')
sns.countplot(x='sex',data=tips)

#TICKS
#Delete ticks (borders with ticks)
#You specify which ones. Usually right & up true in default. Left&bottom need to be declared.
sns.countplot(x='sex',data=tips)
sns.despine(left=True,bottom=True)

#SIZE & ASPECT
#Grid type plot
sns.lmplot(x='total_bill',y='tip',size=2,aspect=4,data=tips)

#CONTEXT & FONT
# Can change the context, according to what you need to do with the graph
# Context parameters: paper, notebook, talk, poster (big visual)
# FONT size change with "font_scale"
sns.set_context('notebook',font_scale=2)
sns.countplot(x='sex',data=tips)

#COLOR
# Change color with "palette"
# Matplotlib colormap: plasma, inferno, magma, viridis, seismic, coolwarm,spectral
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='seismic')