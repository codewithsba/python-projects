import random

secret_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
    except ValueError:
        print("That's not a valid number! Please enter a number.")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if guess == secret_number:
        print("Congratulations! You've guessed the number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
