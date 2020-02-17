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
#  Problem 1 - Backwards
# -------------------------------

forward = "Bentley"
reverse = "".join(reversed(forward))
print(reverse)

# -------------------------------
#  Problem 2 - Threes
# -------------------------------

rolls = input("Enter a sequence of rolls: ")
one = rolls.count("1")
six = rolls.count("6")
print("The total number of 1's and 6's is:", one + six)

# -------------------------------
#  Problem 3 - String Parts
# -------------------------------

s = "Programming in Python"
print("#1 the string:", s)
print("#2 the length of the string:", len(s))
print("#3 the position where \"in\" appears the first time is:", s.find("in"))
print("#4 the number of times \"n\" appears is:", s.count("n"))
print("#5 the number of spaces is:", s.count(" "))
print("#6 the substring \"Pro\":", s[0:3])
print("#7 the substring \"thon\":", s[-4:])
print("#8 the substring \"Programming in Py\":", s[0:17])
print("#9 split the string at the spaces:", s.split(" "))
print("#10 the substring \"a\":", s[5:6])
print("#11 the string in uppercase:", s.upper())
print("#12 the string in lowercase:", s.lower())
print("#13 the string but replace \" in \" with \" with \":", s.replace(" in ", " with "))

# -------------------------------
#  Problem 4  – String Parts
# -------------------------------

string = input("Enter a sentence: ")
word = input("Enter a word from the sentence: ")
print("The number of occurrences of the selected word in the sentence:", string.count(word))

# -------------------------------
#  Exercise #5
# -------------------------------

new_string = input("Enter a string: ")
lowercase_count = 0
uppercase_count = 0
numbers_count = 0
for lower in new_string:
    if lower.islower():
        lowercase_count += 1
for upper in new_string:
    if upper.isupper():
        uppercase_count += 1
for numbers in new_string:
    if numbers.isnumeric():
        numbers_count = numbers_count + 1

print("Number of lowercase characters:", lowercase_count)
print("Number of uppercase characters:", uppercase_count)
print("Number of digits:", numbers_count)

# -------------------------------
#  Exercise #6
# -------------------------------

multiple_letters = input("Enter a string: ")
character_to_replace = input("Enter the character to replace: ")
character_replacing = input("Enter the character to replace it with: ")
print("The new string is: ", multiple_letters.replace(character_to_replace, character_replacing))
