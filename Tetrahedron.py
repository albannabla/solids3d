import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

v = [(0,-1,-1),(0,1,-1),(-1,0,1),(1,0,1)]
g = [[2,3,0],[1,3,0],[1,2,0],[1,2,3]]
v = np.array(v)
a = ["yellow","orange","blue","green"]

fig = plt.figure()
ax = fig.add_subplot((111),projection='3d')
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2, 2)
ax.set_zlim3d(-2, 2)
for f in range(4):
    c=Poly3DCollection([[tuple(y) for y in v[g[f],:]]], linewidths=1, alpha=1)
    c.set_facecolor([a[f]])
    ax.add_collection3d(c)
plt.show()