# accept users coins


def main():
    balance = 0  
    cost = 50
    while balance < cost:
        deposit = int(input("Please insert a coin. (25 | 10 | 5 cents): "))
        
        match deposit:
            case 25 | 10 | 5:
                balance += deposit
                amount_due = cost - balance
                if balance < cost:
                    print("amount_due:", amount_due)
                continue
            case _:
                print("please insert a valid coin.")
        
    if balance > 50:
            amount_due = balance - 50
            print("your change sir:", amount_due)
        







    
main()

        






     
    

# check if the coins are the right denomination. .25, .10 .05





# tell customer amount due to reach .5 dollars



# tell customer change due.