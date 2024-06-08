def tipConverter(cost, percent):
    return float(cost) * float(percent / 100)

meal_cost = int(input('how much was your meal?: '))
tip_percent = int(input('which percent would you like to tip?: '))



print(tipConverter(meal_cost, tip_percent), "$, is your tip amount.")


