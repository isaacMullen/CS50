items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        order = input("Item: ").title()
    except TypeError:
        pass
    except KeyboardInterrupt:
        break
    
    if order in items:
            total += float(items.get(order))
            formatted_total = "%.2f" % total        # formatting the total to display the first 2 decial points regardless of rounded or not. 
            print(f"Total: ${formatted_total}")
      