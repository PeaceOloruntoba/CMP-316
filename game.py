#Python Program to generate a random number between 1 & 50, guess the random number generated, try only five times, if it's correct, you win, if not you loose
import random

# Introducing users 
intro = '''
Welcome to Peace Guessing Game.
You have only 5 chances to guess the correct number.
Good luck playing
'''
print(intro)
# Game Function Definition
def guess_number():
    # Generate a random number between 10 and 30
    secret_number = random.randint(1, 50)

    # Allow the user three attempts to guess the number
    for _ in range(5):
        guess = int(input("Guess the number between 1 and 50: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            return
        elif guess < secret_number:
            print("Your guess is low, Try again!")
        else:
            print("Your guess is high, try again!")

    # If the loop completes without a correct guess
    print(".............................................................")
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Call the function to start the game
guess_number()
