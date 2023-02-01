money = 0
hasScissors = False

while(True):
    
    user_choice = input("[1] Cut Lawns with Teeth [2] Buy Scissors ($5) [3] Cut Lawns with Scissors")
    
    if (user_choice == "1"):
        money += 1
        
        print("You cut the lawn with your teeth and earned $1! Total money: " + str(money))
        
    if (user_choice == "2"):
        if (money >= 5):
            money -= 5
            hasScissors = True
            print(hasScissors)
        else:
            print("Not enough money. Cut more lawns!")