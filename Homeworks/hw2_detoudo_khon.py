"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Coding with Strings

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.
"""
print('Welcome to LaptopConfig.com\n')

total = 0

print('Which model?\nA - Low-End\nB - Productivity\nC - UltraThin')
model = input('Enter your choice: \n')

# Model if statements
if model == 'a':
    total += 599.99
elif model == 'b':
    total += 699.99
elif model == 'c':
    total += 899.99
else:
    exit('You entered an incorrect value. The program will end.')

print('Which operating system?\nA - None (subtract $50)\nB - Windows (included)\nC - Enterprise (add $120)')
operating_system = input('Enter your choice: ')
if operating_system == 'a':
    total -= 50
elif operating_system == 'b':
    total += 0
elif operating_system == 'c':
    total += 120
else:
    exit('You entered an incorrect value. The program will end.')

print('Which storage option?\nA - 128 GB SSD (subtract $40)\nB - 256 GB SSD (standard)\nC - 512 GB SSD (add $100)')
storage_option = input('Enter your choice: ')
if storage_option == 'a':
    total -= 40
elif storage_option == 'b':
    total += 0
elif storage_option == 'c':
    total += 100
else:
    exit('You entered an incorrect value. The program will end.')

print('Which processor?\nA - Core I3 (subtract $60)\nB - Core I5 (standard)\nC - Core I7 (add $120)')
processor = input('Enter your choice: ')
if processor == 'a':
    total -= 60
elif processor == 'b':
    total += 0
elif processor == 'c':
    total += 120
else:
    exit('You entered an incorrect value. The program will end.')

print('How much RAM?\nA -  8 GB RAM (subtract $30)\nB - 16 GB RAM (standard)\nC - 32 GB RAM (add $72)')
RAM = input('Enter your choice: ')
if RAM == 'a':
    total -= 30
elif RAM == 'b':
    total += 0
elif RAM == 'c':
    total += 72
else:
    exit('You entered an incorrect value. The program will end.')

print('*'*52)
print('{:^52s}'.format('Your Order from LaptopConfig.com:'))

if model == 'a':
    print('Laptop Model:', 'Low-End', '$599.99')
elif model == 'b':
    print('Laptop Model:', 'Productivity', '$699.99')
else:
    print('Laptop Model:', 'UltraThin', '$899.99')

if operating_system == 'a':
    print('Operating System:', 'None', '$-50.00')
elif operating_system == 'b':
    print('Operating System:', 'Windows', '$0.00')
else:
    print('Operating System:', 'Enterprise', '$120.00')

if storage_option == 'a':
    print('Storage:', '128 GB SSD', '$-40.00')
elif storage_option == 'b':
    print('Storage:', '256 GB SSD', '$0.00')
else:
    print('Storage:', '512 GB SSD', '$100.00')

if processor == 'a':
    print('Processor:', 'Core I3', '$-60.00')
elif processor == 'b':
    print('Processor:', 'Core I5', '$0.00')
else:
    print('Processor:', 'Core I7', '$120.00')

if RAM == 'a':
    print('RAM:', '8 GB RAM')
elif RAM == 'b':
    print('RAM:', '16 GB RAM', '$0.00')
else:
    print('RAM:', '32 GB RAM', '$72.00')

print('='*52)
print('Total Price:', '$', total)
