# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 18:52:42 2025

@author: meowm
"""

import math
import matplotlib.pyplot as plt

# Hàm sinh thiên hà fractal nâng cấp: chia nhánh + xoắn ốc + định hướng sinh học 3–6–9
def galaxy_fractal_spiral(level=1, base_mass=1e11, angle_offset=0, base_radius=30):
    """
    Tạo ra một cấu trúc fractal thiên hà xoắn ốc 3–6–9
    """
    branches = 3 ** level
    galaxies = []

    for i in range(branches):
        # Tính góc phân bố + độ lệch xoắn ốc nhẹ
        angle = angle_offset + 2 * math.pi * i / branches
        radius = base_radius * level * (1 + 0.2 * math.sin(i))

        # Tính toạ độ xoắn ốc
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        offset_mass = base_mass * (0.9 + 0.2 * math.sin(i))
        galaxies.append({
            'x': x,
            'y': y,
            'mass': offset_mass,
            'level': level,
            'angle': angle,
            'children': galaxy_fractal_spiral(level-1, offset_mass/3, angle_offset=angle, base_radius=base_radius * 0.7) if level > 1 else []
        })
    return galaxies

# Hàm vẽ thiên hà fractal dạng xoắn ốc
def plot_spiral_galaxy(galaxies, parent=None):
    for galaxy in galaxies:
        x, y = galaxy['x'], galaxy['y']
        if parent:
            plt.plot([parent[0], x], [parent[1], y], color='lightblue', linewidth=0.6)
        plt.scatter(x, y, s=4 + galaxy['mass']/1e11, color='midnightblue')
        plot_spiral_galaxy(galaxy['children'], (x, y))

# Sinh dữ liệu và vẽ thiên hà fractal dạng xoắn ốc
spiral_galaxies = galaxy_fractal_spiral(level=3)
plt.figure(figsize=(10, 10))
plot_spiral_galaxy(spiral_galaxies)
plt.title("Fractal Spiral Galaxy Formation - Level 3", fontsize=14)
plt.axis('off')
plt.show()
