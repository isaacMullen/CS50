import random

while True:
    try:
        level = int(input("Level: "))
        answer = random.randint(1, level)
    except ValueError:
        continue
    else:
        break

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess > 0:
        if guess == answer:
            print("Just Right!")
            quit()
        elif guess < answer:
            print("Too Small!")
        else:
            print("Too Large!")
    else:
        continue

