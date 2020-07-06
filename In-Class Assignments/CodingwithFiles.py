"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Coding with Files Class Assignment

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.
"""
# ---------------
# Problem 1
# ---------------
with open('mbox.txt', 'r+') as f:
    count = 0
    for line in f:
        if '@uct.ac.za' in line:
            count += 1
            print(line)
    print('The number of lines with string \"@uct.ac.za\" in it is:', count)
# ---------------
# Problem 2
# ---------------
with open('news_article.txt', 'r+') as f:
    file = f.read().split()
    counter = {}
    for word in file:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1
print(counter)

# --------------
# Problem 3
# --------------
with open('news_article.txt', 'r+') as f:
    file = f.read().split()
    five_words = []
    for words in file:
        if len(word) == 5:
            if word not in five_words:
                five_words.append(word)
    with open('five_letter_words.txt', 'r+') as f:
        f.write(str(five_words))


