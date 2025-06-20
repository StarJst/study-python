# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 18:35:07 2025

@author: meowm
"""

import numpy as np

# Hàm xoắn ốc vàng (logarithmic spiral) để nâng cấp layout thiên hà
def golden_spiral_points(n_points, growth=0.15, turns=3):
    """
    Tạo điểm theo xoắn ốc vàng - golden spiral
    """
    theta = np.linspace(0, 2 * np.pi * turns, n_points)
    r = np.exp(growth * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# Vẽ xoắn ốc vàng nâng cấp dựa trên tư duy fractal 3–6–9
def plot_fractal_spiral(level=3):
    plt.figure(figsize=(10, 10))
    n_total = 3 ** level
    colors = plt.cm.viridis(np.linspace(0, 1, n_total))
    
    for branch in range(n_total):
        growth = 0.15 + 0.02 * (branch % 3)  # Nhịp tăng cho mỗi nhánh
        turns = 1.5 + 0.2 * (branch % 3)     # Vòng xoắn thay đổi chút để tạo nhiễu tự nhiên
        x, y = golden_spiral_points(100, growth=growth, turns=turns)
        plt.plot(x, y, color=colors[branch], linewidth=0.8)
        plt.scatter(x[::20], y[::20], s=3, color=colors[branch], alpha=0.6)

    plt.title("Fractal Galaxy with Golden Spirals (3–6–9 Pattern)", fontsize=14)
    plt.axis('off')
    plt.show()

# Vẽ phiên bản nâng cấp
plot_fractal_spiral(level=3)
