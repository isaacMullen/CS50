def fuel_fraction_to_percent():
    while True:
        fuel = input("Fuel as a fraction: ")
        try:
            x, y = int(fuel.split("/")[0]), int(fuel.split("/")[1])
            if x <= y:
                fuel_percentage = int(x) / int(y)
                return round(fuel_percentage * 100)
        except (ZeroDivisionError, ValueError):
            pass

def main():
    f = fuel_fraction_to_percent()
    if f <= 1:
        print("E")
    elif f >= 99:
        print("F")
    else:
        print(f"{f}%")

main()

