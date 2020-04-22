from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 1, 10)
Y = np.linspace(0, 1, 10)
X, Y = np.meshgrid(X, Y)
Z = np.exp(X+Y)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.copper_r)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()