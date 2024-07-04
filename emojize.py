import emoji        # importing emoji package after pip installing it

while True:
    try:
        emoji_input = emoji.emojize(input("Emoji code or Alias: "), language="alias")       # setting a variable to the users input and turning it into an emoji, if possible, using its alias or code.
    
    except KeyboardInterrupt:       # accepting a CTRL + C to exit the program
        quit()      
    
    if emoji.is_emoji(emoji_input):     # checking if the emoji code or alias was valid and printing the corresponding emoji if true
        print(emoji_input)
    
    else:       # handling cases where the input did not match a code or alias and letting the user know, thereafter continuing the while loop for another input
        print("Enter valid code/Alias.")
        continue

    
    