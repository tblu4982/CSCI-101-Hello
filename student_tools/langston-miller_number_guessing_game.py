TOOL_NAME = "Number Guessing Game"

# This is needed for the program to work.
import random, math

# Looping
running = True

def run():
    guess = 0

    while guess < 1 or guess > 10:
        guess = input("Guess a random number from 1 to 10... ")

        try:
            guess = int(guess)

            if guess < 1 or guess > 10:
                print("Out of range!")
        except:
            print("Invalid input!")
            guess = 0
    
    # Pick the number
    selectedNumber = math.floor(random.random() * 10) + 1

    # Print the message based on the result.
    if selectedNumber == guess:
        print("Wow! You got it correct!")
    else:
        print("Sorry, you lost! The real number was: " + str(selectedNumber))

    running = input("Would you like to quit? (y/n)") != "y"

if __name__ == "__main__":
    while running:
        run()