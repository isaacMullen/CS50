def main():
    fuel_fraction = input("Fuel: ")
    f = convert(fuel_fraction)
    fuel_level = guage(f)
    print(fuel_level)


def convert(f):
    num1, num2 = f.split("/")[0], f.split("/")[1]
    fuel_percentage = (int(num1) / int(num2)) * 100
    if int(num1) < int(num2):
        return round(fuel_percentage)
    else:
        raise ValueError


def guage(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return percentage




if __name__ == "__main__":
   main()

