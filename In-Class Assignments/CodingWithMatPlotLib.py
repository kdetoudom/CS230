"""
Author: Konnie Detoudom
Description: Coding with MatPLotLib
"""
import csv
import numpy as np
from matplotlib import pyplot as plt

# -------------
# Problem 1
# -------------
x = [i for i in range(0, 51)]
y = [i**2 for i in range(0, 51)]


def lineplot():
    plt.plot(x, y, color='c')
    plt.xlabel('X = Axis')
    plt.ylabel('Y - Axis')
    plt.title('My First Line Graph')
    plt.show()


lineplot()
for i in range(len(x)):
    print(x[i], y[i])


# -------------
# Problem 2
# -------------
with open('HistoricalGasPrices.csv', 'r') as csvfile:
    plots = list(csv.reader(csvfile, delimiter=','))
    data_1994 = plots[:][2]
    data_1994 = [int(i) for i in data_1994]
    data_2008 = plots[16][1:]
    data_2008 = [int(i) for i in data_2008]
    months = plots[0][1:]

# Graph 1 - Comparing Gas Prices in 1994 and 2008
fig, ax = plt.subplots()
ax.plot(months, data_1994, marker='o', color='c')
ax.plot(months, data_2008, marker='o',  color='r')
plt.xlabel('Months')
plt.ylabel('Gas Prices')
plt.title('Historical Gas Prices in 1994 and 2008')
plt.legend(labels=['1994', '2008'])
plt.show()

# Graph 2 - All the Gas Prices from 1993 to March of 2020
data = []
for i, row in enumerate(plots):
    if i != 0:
        data += [float(price) for price in plots[i][1:]]
plt.plot(data, color='b')
plt.xlabel('Number of Months since January of 1993')
plt.ylabel('Gas Prices')
plt.title('Historical Gas Prices from 1993 to March of 2020')
plt.show()

# -------------
# Problem 3
# -------------
import pandas as pd

df = pd.read_csv('company_sales_data.csv')

# Exercise Question 4
month_list = df['month_number'].tolist()
toothpaste = df['toothpaste'].tolist()

plt.scatter(month_list, toothpaste, label='Tooth paste scatter plot')
plt.xlabel('Month Number')
plt.ylabel('Number of Units Sold')
plt.legend(labels=['Toothpaste Sales Data'], loc='upper left')
plt.title('Tooth Paste Sales Data')
plt.xticks(month_list)
plt.show()
