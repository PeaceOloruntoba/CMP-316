#Python Program to generate a random number between 10 & 30, guess the random number generated, try only three times, if it's correct, you win, if not you loose
import random

# Game Function Definition
def guess_number():
    # Generate a random number between 10 and 30
    secret_number = random.randint(10, 30)

    # Allow the user three attempts to guess the number
    for _ in range(3):
        guess = int(input("Guess the number between 10 and 30: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            return
        else:
            print("Incorrect guess. Try again.")

    # If the loop completes without a correct guess
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Call the function to start the game
guess_number()
