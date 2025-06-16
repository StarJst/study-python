# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 00:25:47 2025

@author: meowm
"""

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

X = np.arange(0, width)
Y = np.arange(0, height)
X, Y = np.meshgrid(X, Y)

ax.plot_surface(X, Y, terrain, cmap='terrain')
plt.title("3D Fractal Terrain")
plt.show()
