import itertools as it
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

v=[p for p in it.product((-1,1),(-1,1),(-1,1))]
v=np.array(v)
g = [[0,2,6,4],[0,1,5,4],[0,1,3,2],[2,3,7,6],[4,5,7,6],[1,3,7,5]]
a = [0,1,2,3,4,0]

fig = plt.figure()
ax = fig.add_subplot((111),projection='3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
for f in range(6):
    c=Poly3DCollection([[tuple(y) for y in v[g[f],:]]], linewidths=1, alpha=1)
    c.set_facecolor([(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0)][a[f]])
    ax.add_collection3d(c)
plt.show()