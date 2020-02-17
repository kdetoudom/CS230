"""
guessing game uses while loop
"""
import math
import random
print("Guessing Game.")

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
MAXGUESSES = 5
game_over = False

while not game_over:

    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print(f"Congratulations! You've got it in {count} tries!")
        game_over = True
    if count > MAXGUESSES:
        print(f'Game over! The answer is {myNumber}')
        game_over = True

    count += 1
