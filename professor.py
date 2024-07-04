import random

# prompt user for a level, n (1, 2 or 3)
# randomly generate 10 questions (add 2 numbers where the # of digits in each number is n)
# prompt user to answer these questions
# output "EEE" if answer is incorrect
# allow user up to 3 tries per question, after 3 incorrect guesses. output the answer
# output score/10 after program is finished

def main():
    digits = get_level()
    score = 0
    for _ in range(10):
        tries = 0
        num1, num2 = generate_integer(digits), generate_integer(digits)
        correct_answer = num1 + num2
        while tries < 3:
            try:
                response = int(input(f"{num1} + {num2} = "))
                if response == correct_answer:
                    score += 1
                    break
                else:
                    tries += 1
                    print("EEE")
                    continue
            except ValueError:
                tries += 1
                print("EEE")
                continue
    print(f"{score}/10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in range(1, 4):
            return level
        else:
            continue


def generate_integer(n):
    range_start = 10**(n - 1)
    range_end = (10**n) - 1
    return random.randint(range_start, range_end)


if __name__ == "__main__":
    main()