from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

X = np.linspace(-1, 1, 10)
Y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(X, Y)
Z = -np.sqrt(X**2 + Y**2)

front = []
for i in range(len(X[0])):
    front.append((X[0][i],Y[0][i],Z[0][i]))
front.append((1,-1,-2))
front.append((-1,-1,-2))

back = []
for i in range(len(X[-1])):
    back.append((X[-1][i],Y[-1][i],Z[-1][i]))
back.append((1,1,-2))
back.append((-1,1,-2))

left = []
for i in range(len(X)):
    left.append((X[i][0],Y[i][0],Z[i][0]))
left.append((-1,-1,-2))
left.append((-1,1,-2))

right = []
for i in range(len(X)):
    right.append((X[i][-1],Y[i][-1],Z[i][-1]))
right.append((1,-1,-2))
right.append((1,1,-2))

bottom = []
bottom.append((1,-1,-2))
bottom.append((1,1,-2))
bottom.append((-1,1,-2))
bottom.append((-1,-1,-2))

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-2, 1)
c = Poly3DCollection([front,back,left,right,bottom]) 
c.set_facecolor(["yellow","red","orange","green","brown"])
ax.add_collection3d(c)
surf = ax.plot_surface(X, Y, Z)
plt.show()