import random
number=random.radient(1,10)
number=int(input(guess the number:))
if guess<number:
    print("the number is too low")
elif guess>number:
    print("the number is too high")
else:
    ("yay!you guessed the number")
