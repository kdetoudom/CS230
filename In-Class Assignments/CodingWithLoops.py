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
#  Problem 1
# -------------------------------
numbers = [35, 58, 87, 34, 15, 67, 43, 1, 33, 48]
even_numbers, odd_numbers = 0, 0
for num in numbers:
    if num % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
print("The number of even numbers in the list is", even_numbers)
print("The number of odd numbers in the list is", odd_numbers)

# -------------------------------
#  Problem 2
# -------------------------------
name = input("Enter a name: ")
for n in range(len(name)):
    print(f"The character in position {n} is {name[n]}")

# -------------------------------
#  Problem 3
# -----------------------------
while True:
    phone_number = list(input('Please input a phone number in the format (xxx) xxx-xxx: '))
    if phone_number[0] == '(' and phone_number[4] == ')' and phone_number[5] == ' ' and phone_number[9] == '-' and \
            phone_number[1].isdigit() and phone_number[2].isdigit() and phone_number[3].isdigit() and \
            phone_number[6].isdigit() and phone_number[7].isdigit() and phone_number[8].isdigit() and \
            phone_number[10].isdigit() and phone_number[11].isdigit() and phone_number[12].isdigit():
        print('Thank you')
        break
    else:
        print('Invalid phone number, please try again.')
# -------------------------------
#  Problem 4
# -----------------------------
size = int(input('Enter a size:'))
symbol = input('Enter a symbol: ')
direction = input('Enter a direction (d or u): ')

if direction == 'u':
    for num in range(0, size):
        print(symbol * num)
elif direction == 'd':
    for num in range(size, 0, -1):
        print(symbol * num)
else:
    print('Incorrect direction.')

# -------------------------------
#  Problem 5
# -----------------------------
for a in range(1, 6):
    for b in range(1, 6):
        print(f'{a * b:>2d}', end=" ")
    print()
