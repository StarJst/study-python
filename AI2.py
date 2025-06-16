# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 00:26:11 2025

@author: meowm
"""

def get_color(value):
    if value < -0.05:
        return [0, 0, 0.5]        # Biển sâu
    elif value < 0.0:
        return [0, 0, 1]          # Biển
    elif value < 0.05:
        return [1, 1, 0.5]        # Bãi cát
    elif value < 0.3:
        return [0, 0.8, 0]        # Đồng bằng
    elif value < 0.6:
        return [0.3, 0.2, 0.1]    # Núi
    else:
        return [1, 1, 1]          # Tuyết

colored = np.zeros((height, width, 3))
for i in range(height):
    for j in range(width):
        colored[i][j] = get_color(terrain[i][j])

plt.figure(figsize=(6,6))
plt.imshow(colored)
plt.title("Fractal Terrain (Colored)")
plt.axis('off')
plt.show()
