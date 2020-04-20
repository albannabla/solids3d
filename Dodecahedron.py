import itertools as it
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

v=[p for p in it.product((-1,1),(-1,1),(-1,1))]
g=.5+.5*5**.5
v.extend([p for p in it.product((0,),(-1/g,1/g),(-g,g))])
v.extend([p for p in it.product((-1/g,1/g),(-g,g),(0,))])
v.extend([p for p in it.product((-g,g),(0,),(-1/g,1/g))])
v=np.array(v)
g=[[12,14,5,9,1],[12,1,17,16,0],[12,0,8,4,14],[4,18,19,5,14],[4,8,10,6,18],[5,19,7,11,9],[7,15,13,3,11],[7,19,18,6,15],[6,10,2,13,15],[13,2,16,17,3],[3,17,1,9,11],[16,2,10,8,0]]
a=[2,1,0,3,4,5,0,1,2,3,4,5]

fig = plt.figure()
ax = fig.add_subplot((111),projection='3d')
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2, 2)
ax.set_zlim3d(-2, 2)
for f in range(12):
    c=Poly3DCollection([[tuple(y) for y in v[g[f],:]]], linewidths=1, alpha=1)
    c.set_facecolor([(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0)][a[f]])
    ax.add_collection3d(c)

plt.show()