# Number Guesser
import random
lower = 1
upper = 100

secrect_number = random.randint(lower, upper)
print(f"Guess a number between {lower} and {upper}")

attempts = 0
while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess > secrect_number:
        print("Too High ! Please enter lower number.")
    elif guess < secrect_number:
        print("Too LOw ! Please enter higher number.")
    else:
        print("Congratulations! You guessed it.")
        print(f"Your number is {guess}")
        print(f"You guesed it {attempts}")
        break
