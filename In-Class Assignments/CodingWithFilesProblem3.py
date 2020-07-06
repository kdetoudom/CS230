# -----------
# Problem 3
# -----------
file_to_open = input("Please enter the name of a file to be read: ")
number_of_words = 0

with open(file_to_open, 'r') as f:
    ftext = f.read()
number_of_words = len(ftext.split())

print(f'The number of words in the file is {number_of_words}.')
