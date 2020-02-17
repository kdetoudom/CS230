"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Coding with Strings

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.
"""
# -------------------------------
#  Problem 1 – Woof, Meow, Oink, Moo
# -------------------------------

animal = input('Enter an animal: ')

if animal == 'cow':
    print('A cow goes moo.')
elif animal == 'dog':
    print('A dog goes woof.')
elif animal == 'cat':
    print('A cat goes meow.')
else:
    print('Error: Animal not valid.')

# -------------------------------
#  Problem 2 – Multiple of Three?
# -------------------------------

number = int(input('Please enter a number: '))

if number % 3 == 0:
    print(f'{number} is a multiple of three')
else:
    print(f'{number} is not a multiple of three')

# -------------------------------
#  Problem 3 – Day of the Week
# -------------------------------
number_of_the_week = int(input('Enter a number 1 through 7: '))

if number_of_the_week == 1:
    print(f'{number_of_the_week} is Sunday')
elif number_of_the_week == 2:
    print(f'{number_of_the_week} is Monday')
elif number_of_the_week == 3:
    print(f'{number_of_the_week} is Tuesday')
elif number_of_the_week == 4:
    print(f'{number_of_the_week} is Wednesday')
elif number_of_the_week == 5:
    print(f'{number_of_the_week} is Thursday')
elif number_of_the_week == 6:
    print(f'{number_of_the_week} is Friday')
elif number_of_the_week == 7:
    print(f'{number_of_the_week} is Saturday')
else:
    print('Invalid Number')

# -------------------------------
#  Problem 4  – Buy a Vowel
# -------------------------------
phrase = input('Enter a phrase: ')
letter = input('Enter a letter: ')

if letter in phrase:
    print(letter.upper(), 'appears', phrase.count(letter), 'times.')
if letter in 'aeiou':
    print('The cost of', letter.upper(), 'is', int(phrase.count(letter)) * 250)
else:
    print('The letter is not in the word.')

# -------------------------------
#  Problem 5  – Time and a Half
# -------------------------------

weekday = input('Enter days worked: ')
hours = int(input('Enter hours worked: '))
HOURLYRATE = 16
total = 0
overtime_hours = 0
bonus = 0

if hours > 40:
    overtime_hours = hours - 40
    hours = 40
if 'U' in weekday and 'S' in weekday:
    bonus += 125
elif 'U' in weekday or 'S' in weekday:
    bonus += 50

total = int(hours * HOURLYRATE + overtime_hours * 1.5 * HOURLYRATE + bonus)

print(f'Your pay is: ${total:.2f}')
