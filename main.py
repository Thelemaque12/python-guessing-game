import random

name = input("what is your name: ")
secretNumber = random.randint(1,30)
print(f"hello welcome {name}")
for guessNumber in range(1, 7):
    guess = int(input("enter a guessing number "))
    if guess > secretNumber:
        print("guess number is too high")
    elif guess < secretNumber:
        print("guess number is too low")
    else:
        break
if guess == secretNumber:
    print(f"wow you guessed it")
else:
    print(f"sorry you're out of tries the secret number is {secretNumber}")