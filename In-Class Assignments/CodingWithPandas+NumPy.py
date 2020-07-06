"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Homework - Coding with Pandas and Numpy

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataset = 'gpa.csv'
df = pd.read_csv(dataset)

max_value = df['GPA'].max()
min_value = df['GPA'].min()
avg_value = df['GPA'].mean()
max_name = df['Name'][df['GPA'] == max_value].values
df = df.sort_values(by=['GPA', 'Name'], ascending=[False, True])
df.at[5, 'GPA'] = 2.3
row_four = df.iloc[4]


print(f"The maximum GPA is {max_value}, the minimum is {min_value}, and the mean is {avg_value:.2f}.")
print(f"The name(s) of the students with the max GPA is/are {max_name}.")
print(df)
print(row_four)

names = df.loc[:, 'Name']
gpa = df.loc[:, 'GPA']
age = df.loc[:, 'Age']

plt.bar(names, gpa, color='r')
plt.title('GPA of Each Student')
plt.xlabel('Name of Student')
plt.ylabel('GPA on a 4.0 Scale')
plt.show()

plt.scatter(age, gpa, color='c')
plt.title('Age to GPA')
plt.xlabel('Age')
plt.ylabel('GPA')
plt.show()
