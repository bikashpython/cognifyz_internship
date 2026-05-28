# Guessing Number
import random

Number = random.randint(1, 100)
while True:
    Guess = int(input("Guess the number (1- 100): "))
    
    if Guess > Number:
        print("Too High !")
    elif Guess < Number:
        print("Too low !")
    else:
        print("Congratulation ! You guessed it. ")
        break