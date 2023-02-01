money = 0

while(True):
    
    user_choice = input("[1] Cut Lawn")
    
    if (user_choice == "1"):
        money += 1
        
        print("You cut the lawn with your teeth and earned $1! Total money: " + str(money))