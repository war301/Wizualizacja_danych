import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

###lab1
plt.figure().gca(projection = "3d")

z = np.linspace(0, 2*np.pi, 100)
x = np.sin(z)
y = 2*np.cos(z)

plt.plot(x, y, z)
plt.show()
###lab2
ax = plt.subplot(111, projection="3d")

color = ["r", "b", "m", "c", "g"]
marker = [".", "h", "X", "D", "*"]

for i in range(5):
    x = (100 - 0) * np.random.rand(100) + 0
    y = (100 - 0) * np.random.rand(100) + 0
    z = (100 - 0) * np.random.rand(100) + 0
    ax.scatter(x, y, z, c=color[i], marker=marker[i])

plt.show()
###lab3
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

#####^
ax = plt.subplot(231, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="coolwarm",
linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
plt.colorbar(surf, shrink=0.5, aspect=5)
#####^
ax = plt.subplot(232, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="Greys",
linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
plt.colorbar(surf, shrink=0.5, aspect=5)
#####^
ax = plt.subplot(233, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="cool",
linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
plt.colorbar(surf, shrink=0.5, aspect=5)
#####^
ax = plt.subplot(234, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="hsv",
linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
plt.colorbar(surf, shrink=0.5, aspect=5)
#####^
ax = plt.subplot(235, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="rainbow",
linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
plt.colorbar(surf, shrink=0.5, aspect=5)
#####^
ax = plt.subplot(236, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="ocean",
linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
plt.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
###lab4
fig = plt.figure(figsize =(8, 3))
ax1 = plt.subplot(231, projection="3d")
ax2 = plt.subplot(232, projection="3d")
ax3 = plt.subplot(233, projection="3d")
ax4 = plt.subplot(234, projection="3d")
ax5 = plt.subplot(235, projection="3d")
ax6 = plt.subplot(236, projection="3d")

_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax2.bar3d(x, y, bottom, width, depth, top, shade=True, color="m")
ax3.bar3d(x, y, bottom, width, depth, top, shade=True, color="c")
ax4.bar3d(x, y, bottom, width, depth, top, shade=True, color="r")
ax5.bar3d(x, y, bottom, width, depth, top, shade=True, color="g")
ax6.bar3d(x, y, bottom, width, depth, top, shade=True, color="b")
plt.show()
###lab5
#####^
ax = plt.subplot(121, projection="3d")

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, cmap="coolwarm", linewidth=0, antialiased=False)
ax.set_zlim(-1.01 , 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.colorbar(surf, shrink=0.5, aspect=5)
#####^
ax = plt.subplot(122, projection="3d")

X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, cmap="coolwarm", linewidth=0, antialiased=True)
ax.set_zlim(-1.01 , 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
###lab6
ax = plt.subplot(121, projection="3d")

x = (100 - 0) * np.random.rand(20) + 0
y = (100 - 0) * np.random.rand(20) + 0
z = (100 - 0) * np.random.rand(20) + 0
ax.scatter(x, y, z, c="r")

ax = plt.subplot(122, projection="3d")

x = (100 - 0) * np.random.rand(5) + 0
y = (100 - 0) * np.random.rand(5) + 0
z = (100 - 0) * np.random.rand(5) + 0
ax.plot(x, y, z, c="g")

plt.show()
###lab7
ax = plt.subplot(111, projection="3d")

x = (100 - 0) * np.random.rand(20) + 0
y = (100 - 0) * np.random.rand(20) + 0
z = (100 - 0) * np.random.rand(20) + 0
ax.scatter(x, y, z, c="r", label="Jablko")

x = (100 - 0) * np.random.rand(5) + 0
y = (100 - 0) * np.random.rand(5) + 0
z = (100 - 0) * np.random.rand(5) + 0
ax.plot(x, y, z, c="g", label="Waz")

plt.legend()
plt.title("Snake")

plt.show()
