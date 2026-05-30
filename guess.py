import random
number = random.randint(0, 100)
print("Welcome to the Number Guessing Game!")
guess = int(input("Guess a number between 0 and 100: "))
i = 0
while guess != number:
    if guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 0 and 100: "))
    i = i + 1

print("Congratulations! You guessed the number correctly. The number was:", number)
print("It took you", i, "guesses.")