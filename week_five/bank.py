def main():
    userGreeting = input("What word would you use to Greet someone?: ")
    userGreeting = userGreeting.lower()
    print(value(userGreeting))
        

def value(str = "hello"):
    if str.split()[0] == "hello":  
        return 0
    elif str.strip()[0] == "h":             
        return 20                                  
    else:                           
        return 100
 
if __name__ == "__main__":
    main()
    



