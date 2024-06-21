months = [          # list of months to verify input with
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"

]

print("CTRL + C to quit.\n")        


while True:
    # trying to get input from the user, fomatted in a specific manner.
    try:
        date = input("Date formatted as MM/DD/YYYY or Month DD, YYYY: ")
    # catching a KeyboardInterrupt at the input stage so as to cleanly quit the program.
    except KeyboardInterrupt:       
        quit()
    # checking for "/" in the string, if found we assign 3 new varaibles to hold the values of MM DD and YYYY without the "/"
    if "/" in date:
        month, day, year = date.split("/")
        # checking if the month and day entries are valid integers, either 1-31 or 1-12. printing a formatted string to correctly display the date in a more computer friendly manner
        if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
            print(f"{year}-{int(month):02}-{int(day):02}")
    
    # handling the case where date was formatted as MONTH DD, YYYY 
    elif "," in date:       
        # getting rid of the "," for clean printing later on
        date = date.replace(",", "")            
        # splitting by the default character of a white space to seperate our values and assign them to variables
        month, day, year = date.split()     
        # assigning "index" the index of the entered month and adding 1 to adjust for the index starting at 0 given no such "month 0" exists. catching a ValueError if the month can't be found within the list
        try:
            index = months.index(month) + 1
        except ValueError:
            continue
        # assuring the day and month number make sense again. printing a formatted string to correctly display the date in a more computer friendly manner
        if 1<= int(day) <= 31 and 1 <= index <= 12:
            print(f"{int(year):02}-{index:02}-{int(day):02}")
      
            




    