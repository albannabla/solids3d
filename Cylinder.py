import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# create the side of the barrel
alpha = np.linspace(0, 2*np.pi, 50)
x = np.zeros([2,50])
y = np.zeros([2,50])
height = np.zeros([2,50])
height[1] = np.ones(50)
for i in range(len(height)):
    x[i] = np.cos(alpha)
    y[i] = np.sin(alpha)

# create the top and bottom
z = [1,0]
v_1 = []
v_2 = []
for i in range(len(alpha)):
    v_1.append((np.cos(alpha[i]),np.sin(alpha[i]),z[0]))
    v_2.append((np.cos(alpha[i]),np.sin(alpha[i]),z[1]))

# plot all of them
fig = plt.figure()
ax = fig.add_subplot((111),projection='3d')
ax.plot_surface(x,y,height)
c = Poly3DCollection([v_1,v_2], linewidths=1, alpha=1)
c.set_facecolor(["yellow","red"]) 
ax.add_collection3d(c)
plt.show()