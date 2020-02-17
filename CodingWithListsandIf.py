"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Coding with Strings

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.
"""
#-------------------------------
#  Problem 1 – Same Number?
#-------------------------------
number_one = int(input("Enter a number: "))
number_two = int(input("Enter a second number: "))

if number_one == number_two:
    print(f"{number_one} is equal to {number_two}")
else:
    print(f"{number_one} is not equal to {number_two}")

# -------------------------------
#  Problem 2 – Sum of Two
# -------------------------------
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the final number: "))

first_and_second = first_number + second_number
first_and_third = first_number + third_number
second_and_third = second_number + third_number

if first_and_second or first_and_third or second_and_third >= third_number:
    print(f"The sum is greater than or equal to {third_number}")
else:
    print(f"The sum is not greater than or equal to {third_number}")

# -------------------------------
#  Problem 3 – Smallest
# -------------------------------
one = int(input("Enter a number: "))
two = int(input("Enter another number: "))
third = int(input("Enter the last number: "))

if one > two:
    print(f"The smallest number is {two}")
else:
    if one < third:
        print(f"The smallest number is {one}")
    else:
        print(f"The smallest value is {third}")

# -------------------------------
#  Problem 4 – Palindrome
# -------------------------------

string_one = input("Enter a phrase: ")
string_two = input("Enter another phrase: ")

if string_one[::-1] == string_one:
    print(f"{string_one} is a palindrome")
else:
    print(f"{string_one} is not a palindrome")

if string_two[::-1] == string_two:
    print(f"{string_two} is a palindrome")
else:
    print(f"{string_two} is not a palindrome")
