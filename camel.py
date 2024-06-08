
camel_case_name = input("name a variable using camelCase notation: ")


def snake_case_name(name):
    for letter in (name):
        if letter.isupper():
            print("_", letter.lower(), end="")
        else:
            print(letter, end="")
    print()
        
snake_case_name(camel_case_name)
        
