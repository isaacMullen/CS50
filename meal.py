def convert(time):
    float_minute = float(time[1])
    float_hour = float(time[0])
    float_minute /= 60
    time = float_hour + float_minute
    return time
    

def main(x):
    if 7 <= x <= 8:
        print("Breakfast time.")
    elif 12 <= x <= 13:
        print("Lunch time.")
    elif 18 <= x <= 19:
        print("Dinner time.")
    else:
        return

starting_time = input("what time is it right now?: ")

split_time = starting_time.split(":")

time = convert(split_time)

print (round(time, 2))

main(float(time))








    




