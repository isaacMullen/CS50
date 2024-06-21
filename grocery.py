food_list = []

shopping_list = {}

while True:
    try:
        food_item = input("Food item: ")

    except KeyboardInterrupt:
        print()
        break

    food_list.append(food_item)

for item in food_list:
    #shopping_list[item] = shopping_list.get(item, 0) + 1
    if item in shopping_list:
        shopping_list[item] += 1
    else:
        shopping_list[item] = 1
    
    

for item in shopping_list:
    print(shopping_list[item], item.upper())






    