def main():
    userInput = input("What is the answer to the Great Question of Life, the Universe, and Everything?: ")
    
    print (type(userInput)) #Verifies the data type, should always be string in this case. (TEST)
    
    match userInput.lower():
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("nope.")
main()

        