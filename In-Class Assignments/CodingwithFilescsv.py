"""
Author: Konnie Detoudom
Description: Coding with Files Class 2 (CSV Exercise)
"""

import csv
# -----------
# Problem 2
# -----------
file_to_read = input("Enter name of your 'csv_file': ")
thin_mints = 0
peanut_butter = 0
shortbread = 0

try:
    with open(file_to_read, 'r') as csv_file:
        data = csv.reader(csv_file)
        list_row = 0
        header = None
        for i, row in enumerate(data):
            if i == 0:
                header = row
            else:
                thin_mints += int(row[1])
                peanut_butter += int(row[2])
                shortbread += int(row[3])
        print(f'There were {thin_mints} Thin Mints, {peanut_butter} Peanut Butter Cookies, and {shortbread} Shortbread Cookies sold.')

except FileNotFoundError:
    print('Something went wrong. That file does not exist.')

