# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 00:22:36 2025

@author: meowm
"""

import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

# Kích thước bản đồ
width = 200
height = 200

# Thông số noise
scale = 50.0        # độ "zoom"
octaves = 6         # số lớp lặp fractal
persistence = 0.5   # ảnh hưởng của các lớp cao
lacunarity = 2.0    # độ "phân nhánh" của fractal

# Tạo mảng lưu giá trị địa hình
terrain = np.zeros((height, width))

# Tạo fractal noise
for i in range(height):
    for j in range(width):
        x = i / scale
        y = j / scale
        terrain[i][j] = pnoise2(x, y, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=1024, repeaty=1024, base=42)

# Vẽ bản đồ địa hình
plt.figure(figsize=(6,6))
plt.imshow(terrain, cmap='gray')  # Dùng bản đồ màu xám
plt.title("Fractal Terrain (Perlin Noise)")
plt.axis('off')
plt.show()
