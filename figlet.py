from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = Figlet.getFonts(figlet)

valid_font_arguments = ["-f", "--font"]

if len(sys.argv) > 1 and sys.argv[1] not in valid_font_arguments or sys.argv[2] not in fonts:
    print("Invalid usage.")
    sys.exit()

user_input = input("Input: ")

if len(sys.argv) == 1:      
    chosen_font = random.choice(fonts)      
    figlet.setFont(font=chosen_font)        
    
    print(figlet.renderText(user_input))         

elif len(sys.argv) == 3:       
    
    chosen_font = sys.argv[2]                                                                    
    
    figlet.setFont(font=chosen_font)        
    print(figlet.renderText(user_input))       
