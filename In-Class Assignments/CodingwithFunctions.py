def reversing(x):
    return x[::-1]

# -------------------------
# Exercise 2 - Unique List Values
# -------------------------

list = ["This", "This", "is", "is", "a", "list."]


def unique(x):
    list2 = []
    for item in x:
        if item not in list2:
            list2.append(item)
        return list2


print(unique(list))


# -------------------------
# Exercise 3 - Tokenize
# -------------------------

def tokenize(x):
    return x.split()


result1 = tokenize('I like Python')
result2 = tokenize('I like Python', open='[', close=']')
result3 = tokenize("I like Python", open="{", close="}")

print(result1)
print(result2)
print(result3)

