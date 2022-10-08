import random

if __name__ == '__main__':

    targetNum = random.randint(1, 10)
    guess = int(input("Enter Guess: "))
    guessCount = 1

    # Game loop
    while guess != targetNum:

        if guess < targetNum:
            print("Too low!")
            guess = int(input("Enter Guess: "))
            guessCount += 1

        elif guess > targetNum:
            print("Too high!")
            guess = int(input("Enter Guess: "))
            guessCount += 1

    print(f"Correct! It took you { guessCount } guesses!")
