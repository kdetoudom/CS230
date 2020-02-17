"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Coding Problems for Module 2

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.

"""
# --------------------------------
#  Problem 1 - Temperatures
# --------------------------------

print("Please input the temperature in Celsius to convert to Fahrenheit")
celsius = int(input())
fahrenheit = (9/5*celsius + 32)

print("Degrees Fahrenheit: " + str(fahrenheit))
print("Degrees Celsius: " + str(celsius).rjust(4))

# --------------------------------
#  Problem 2 - Building a Fence
# --------------------------------

print("Please input the width of the field")
width = int(input())

print("Please input the length of the field")
length = int(input())

perimeter = (width*2)+(length*2)
print("A field of ", width, " meters by ", length, " meters has a perimeter of ", perimeter, " meters")

# --------------------------------
#  Problem 3 - Birthday Donuts
# --------------------------------
print("Who is having a birthday?")
birthdayName = input()
print("Enter the number of people at the party that will be eating donuts")
numberOfGuests = int(input())
NUMBEROFDONUTS = 24

print("HAPPY BIRTHDAY, " + birthdayName)
print("For ", numberOfGuests, " guests, you will need 2 dozen donuts.")
print("Option 1:   ", int(NUMBEROFDONUTS/numberOfGuests), "donuts each and", int(NUMBEROFDONUTS%numberOfGuests), "donuts left over.")
print("Option 2:   ", "%.2f" % (NUMBEROFDONUTS/numberOfGuests), "donuts each")

# --------------------------------
#  Problem 4 - Change for a 5
# --------------------------------
purchase_amount = float(input("Enter amount of purchase: $"))
FIVEDOLLARS = 5
change = (FIVEDOLLARS-purchase_amount) * 100

print("Change from $5.00 is:")
change_left = change
dollar_bills = change_left // 100
print('%.f Dollar Bills = $%.2f' % (dollar_bills, dollar_bills * 100 / 100))
change_left = change_left - dollar_bills * 100

quarters = change_left // 25
print('%.f Quarters     = $%.2f' % (quarters, quarters * 25 / 100))
change_left = change_left - quarters * 25

dimes = change_left // 10
print('%.f Dimes        = $%.2f' % (dimes, dimes * 10 / 100))
change_left = change_left - dimes * 10

nickels = change_left // 5
print('%.f Nickels      = $%.2f' % (nickels, nickels * 5 / 100))
change_left = change_left - nickels * 5

pennies = change_left // 1
print('%.f Pennies      = $%.2f' % (pennies, pennies * 1 / 100))

print("Total Change:    $%.2f" % (change / 100))

# --------------------------------
#  Problem 5 - Strings
# --------------------------------
string = "Programming in Python"
print(len(string))
print(string[0:3])
print(string[-4:])
print(string[0:17])
print(string.upper())
print(string.lower())
print(string.replace(" in ", " with "))

javaResults = string.startswith("Java")
print(javaResults)

mingResults = string.endswith("ming")
print(mingResults)

# --------------------------------
#  Problem 6 - Digits
# --------------------------------

number = int(input("Enter a number:  "))
str(number)
sum_digits = 0
reverse_number = ''
for c in str(number):
    sum_digits += int(c)
    reverse_number = c + reverse_number
print("The number of its digits is:", sum_digits)
print("The number in reverse is:", reverse_number)
print("The sum of the original number and the reversed number is:", number + int(reverse_number))
