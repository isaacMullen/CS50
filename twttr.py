text = input("Enter a string: ")

for i in text:
    match i:
        case "a" | "e" | "i" | "o"| "u" | "A" |  "E" | "I" | "O"| "U":
            i.replace(i, "")
        
        case _:
            print(i, end="")
        
       


        



   








