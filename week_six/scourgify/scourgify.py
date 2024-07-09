import csv
import sys
import os

# initializing a list which I will populate with dicitonaries -- each dictionary being a student with keys, 'first', 'last' and 'house'.
students = []


def main():
    # checking for correct number or command-line arguments, catching 'IndexError'
    try:
        first_file = sys.argv[1]
        second_file = sys.argv[2]
    except IndexError:
        print("Please enter 2 arguments.")
        sys.exit()
    # setting a varaible which is the file-extension of 2 given files -- if the extensions are '.csv' we run the program
    check_first_file_csv = os.path.splitext(first_file)[1]
    check_second_file_csv = os.path.splitext(second_file)[1]
    if check_first_file_csv == ".csv" and check_second_file_csv == ".csv":
        read_first_file(first_file)
        write_second_file(second_file)
    else:
        print("both files must be a '.csv'")
        sys.exit()


# reads a given .csv file so we can make a list of the key:value pairs
def read_first_file(f):
    with open(f) as file:
        reader = csv.DictReader(file)
        # each row in the file, the 'name' column is split into 'first' and 'last'
        for row in reader:
            last, first = row["name"].split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})


# writes the contents of [students] list into a seperate .csv file
def write_second_file(f):
    with open(f, "w", newline="") as file:
        # setting the fieldnames properly in our new file and writing out the actual fieldnames so we can more easily interpret the data
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        # iterating through the length of the students list and writing the contents of the dictionary into our .csv file row by row.
        for i in range (len(students)):
            writer.writerow({"first": students[i]["first"], "last": students[i]["last"], "house": students[i]["house"]})

if __name__ == "__main__":
    main()