import sys
from tabulate import tabulate
import csv
import os


pizzas = []

def main():
    f = sys.argv[1]
    split_tuple = os.path.splitext(f)
    if len(sys.argv) != 2 or split_tuple[1] != ".csv":
        print("Please enter 1 .csv file.")
        sys.exit()
    make_table(f)
    print(tabulate(pizzas, headers="keys", tablefmt= "simple_grid"))


def make_table(f):
    with open(f) as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizzas.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
        
if __name__ == "__main__":
    main()