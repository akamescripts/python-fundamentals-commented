import random

# generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# initialize the number of guesses
num_guesses = 0

# keep looping until the user guesses the correct number
while True:
    # get the user's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # increment the number of guesses
    num_guesses += 1

    # check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the secret number in", num_guesses, "guesses.")
        break
    elif guess < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
