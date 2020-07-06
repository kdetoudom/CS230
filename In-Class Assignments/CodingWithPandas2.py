"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Coding with Pandas 2

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.
"""
# ------------
# Exercise 1
# ------------
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=exam_data, index=labels, columns=['name', 'score', 'attempts', 'qualify'])
print(df)
print()

# ------------
# Exercise 2
# ------------

print(df.loc[:, ['name', 'score']])
print()

min_attempts = df[df['attempts'] > 2]
print(min_attempts)
print()

missing_score = df[pd.isna(df.score)]
print(missing_score)
print()

df.at['d', 'score'] = 11.5
print(df)
print()

df2 = pd.DataFrame(['Suresh', 15.5, 1, 'yes', 'k'])
df.append(df2)
print(df)

# ------------
# Exercise 3
# ------------
raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons',
                 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
    'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd'],
    'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
    'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
    'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
    'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
    'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
    'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon',
               'Wyoming', 'Louisana', 'Georgia']}

army = pd.DataFrame(data=raw_data, index= raw_data['origin'], columns=['regiment', 'company', 'deaths', 'battles', 'size', 'veterans', 'readiness', 'armored', 'deserters', 'origin'])
soldier_deaths = army[army['deaths'] > 50]
more_soldier_deaths = army[(army['deaths'] > 500) | (army['deaths'] < 50)]
not_dragoons = army[army['regiment'] != 'Dragoons']

print(army.loc[:, ['veterans', 'deaths']])
print(army.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']])
print(army.iloc[3:8, 3:7])
print(army.iloc[4:])
print(army.iloc[:, 3:8])
print(soldier_deaths)
print(more_soldier_deaths)
print(not_dragoons)
print(army.loc[['Texas', 'Arizona']])
