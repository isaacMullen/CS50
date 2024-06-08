def main():
    userGreeting = input("What word would you use to Greet someone?: ")
    userGreeting.lower()
    check_greeting(userGreeting)
        
def check_greeting(str):
    if str.split()[0] == "hello":   # .split() will take the individual words of a string (- blank spaces) and place them in a List. Then I index the list at its first entry and check for 'hello'
        print("0$")
        print(str)
    elif str.strip()[0] == "h":             # (.strip() removes any blank spaces before and after words of a string).. 
                                            # if the first check of 'hello' fails, I will not turn my string into a list, and simply index the first letter of the string, cehcking for an 'h'
        print("20$")
        print(str)
    else:                           # if both previous checks fail, 100$ goes to me since they didn't greet me with an 'h' greeting, nor did they say 'hello'
        print("100$")
        print(str)

main()
    
    



