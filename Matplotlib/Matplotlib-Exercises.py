import matplotlib.pyplot as plt

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


#EXERCISE 1
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
ax.set_ylabel('y')
ax.set_xlabel('x')
ax.set_title('title')

#EXERCISE 2
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])
ax1.plot(x,y,color='red')
ax2.plot(x,y,color='red')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

#EXERCISE 3
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])
ax1.plot(x,z,color='blue',linewidth=0.8,alpha=0.9)
ax2.plot(x,y,color='blue',linewidth=0.8,alpha=0.9)
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')

#EXERCISE 4 (a)
# fig, axes = plt.subplots(nrows=1, ncols=2)
fig, axes = plt.subplots(1,2)
axes[0].plot(x,y,color='blue',lw=2,linestyle='--')
axes[1].plot(x,z,color='red',lw=3)

#EXERCISE 4 (b)
#If plot shows 0 along the axes and not in the corner, use set_xlim & set_ylim to put it in the corner
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9,1.9))
axes[0].plot(x,y,color='blue',lw=4.5)
axes[1].plot(x,z,color='red',lw=2,linestyle='--')
axes[0].set_xlim(0,100)
axes[0].set_ylim(0,200)
axes[1].set_xlim(0,100)
axes[1].set_ylim(0,10000)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
plt.tight_layout()