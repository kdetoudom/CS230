"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Homework 1 - Working with a Calendar - In this program, it works with my birthday and the calendar and will
print out facts about my birthday.

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.

"""
print('Homework #1: Working with a Calendar')
name = input('Enter you full name: ')
birthday = input('Enter you birthday in the form mm/dd/yyyy: ')
today = input('Enter today\'s date in the form mm/dd/yyyy: ')

birthday_dates = birthday.split('/')
quarter = (int(birthday_dates[0]) - 1) // 3 + 1
week = (int(birthday_dates[1]) - 1) // 7 + 1
month = birthday_dates[0]
todays_date = today.split('/')

year = int(todays_date[2]) + 1
if int(todays_date[0]) < int(birthday_dates[0]):
    year -= 1
elif int(todays_date[0]) == int(birthday_dates[0]):
    if int(todays_date[1]) <= int(birthday_dates[1]):
        year -= 1

one_hundred_birthday = int(birthday_dates[2]) + 100
how_many = 100 - (year - int(birthday_dates[2]))

print(f'\nWelcome {name}')
print(f'You were born in quarter {quarter}')
print(f'You were born in week {week}')
print(f'you were born in month {month}')
print('Your next birthday will be on', birthday[0:6] + str(year))
print(name, 'will turn 100 in', how_many, 'years in', one_hundred_birthday)

print('\nGraph for each day of your birth month')
print('*' * int(birthday_dates[1]))
