def calculator(query):
        num1, num2 = float(query[0]), float(query[2])
        
        
        match query[1]:
            case "+":
                print (round((num1 + num2), 1))
            case "x":
                print (round((num1 * num2), 1))
            case "/":
                if num2 == 0:
                    print("cannot divide by 0.. ")
                    return
                else:
                    print (round((num1 / num2), 1))
            case "-":
                print (round((num1 - num2), 1))
        



while True:
    initial_question = input("Enter an arithmetic expression you'd like calculated: ")

    if initial_question == "done":
        break
    new_question = initial_question.split()

    calculator(new_question)

    
        
    






    




    







