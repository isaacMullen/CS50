import sys

# take a command line argument of an existing python file. 
# determine the number of lines of code within the file. 
# exclude comments (lines starting with #), and blank lines from the count.

def main():
    if len(sys.argv) != 2:
        print("Enter (1) command-line arguement.")
    else:
        print(line_counter(), "lines of code.")


def line_counter(): 
    count = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#") or line.strip() == "":
                    pass
                else:
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File not found.")
        

if __name__ == "__main__":
    main()

  
        


