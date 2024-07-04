def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# between 2 and 6 characters
# starts with 2 letters
# first number must not be 0
# no numbers in the middle of plate
# no periods, spaces or punctuation marks

def is_valid(s = "aabc23"):
    if 6 >= len(s) >= 2:    # CHECKING LENGTH
        
        if s.isalpha():     # CHECKING IF WHOLE STRING IS LETTERS
            return True
        elif s.isalnum() and s[0 : 2].isalpha():    # CHECKING IF STRING IS ALPHANUMERIC AND FIRST 2 ARE LETTERS
            
            for char in s:      # ITERATING THROUGH STRING
                
                if char.isdigit():      # CHECKING EACH CHARACTER TO SEE IF IT IS A NUMBER
                    
                    position = s.index(char)        # IF IT'S A NUMBER, SETTING var(POSITION) TO ITS INDEX
                    
                    if s[position: ].isdigit() and int(char) != 0:      # MAKING SURE THE FOLLOWING CHARACTERS ARE ALSO NUMBERS | MAKING SURE FIRST NUMBER ISN'T 0 
                        return True
                    
                    else:
                        return False
        else:
            return False
    else:
        return False
                        

if __name__ == "__main__":
    main()

            
    


