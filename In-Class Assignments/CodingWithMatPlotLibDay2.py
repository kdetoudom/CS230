"""
Author: Konnie Detoudom
Description: Coding with MatPlotLib Day 2
"""
from matplotlib import pyplot as plt
import pandas as pd

# -------------
# Problem 1
# -------------
data = pd.read_csv('Scatter.csv')

height = data['Height'].tolist()
weight = data['Weight'].tolist()

plt.scatter(height, weight, marker='o', color='c', label='Height and Weight of Person')
plt.title('Comparing Heights and Weights')
plt.xlabel('Height', fontsize=14)
plt.ylabel('Weight', fontsize=14)
plt.legend(loc='upper left')
plt.show()

# -------------
# Problem 2
# -------------
x1 = [1, 4, 5, 6, 7]
y1 = [2, 6, 3, 6, 3]
width = 3

plt.plot(x1, y1, width)
plt.title('Line Graph')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.xticks()
plt.show()

# -------------
# Problem 3
# -------------
plt.figure(figsize=(6, 4))
plt.subplot(1, 2, 1)
plt.scatter(height, weight, marker='o', color='c')
plt.title('Comparing Heights and Weights')
plt.xlabel('Height', fontsize=14)
plt.ylabel('Weight', fontsize=14)
plt.legend(loc='upper left', labels='Height and Weight of Person')

plt.subplot(1, 2, 2)
plt.plot(x1, y1, width)
plt.title('Line Graph')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.xticks()
plt.show()
