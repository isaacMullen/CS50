vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def main():
    text = input("Enter a string: ")
    print(shorten(text))



def shorten(s = "aeiou"):
    for letter in s:
        if letter in vowels:
            s = s.replace(letter, "")
    return s
        

if __name__ == "__main__":
    main()

        



   








