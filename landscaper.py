money = 0
hasScissors = False
hasPushLawnMower = False
hasBatPowLawnMower = False
hasTeam = False

while((hasTeam == False) and (money < 1000)):
    
    user_choice = input("[1] Cut Lawns with Teeth \n[2] Buy Scissors ($5) \n[3] Cut Lawns with Scissors \n[4] Buy Push Lawnmower ($25) \n[5] Cut Lawns with Push Lawnmower \n[6] Buy Battery-Powered Lawnmower ($250) \n[7] Cut Lawns with Battery-Powered Lawnmower \n[8] Hire a Team of Starving Students ($500) \n[9] Cut Lawns Using Team of Starving Students \n[10] Check Money ")
    
    if (user_choice == "1"):
        money += 1
        
        print(f"You cut lawns with your teeth and earned $1! Total money: ${money}\n")
        
    if (user_choice == "2"):
        # check if user already has scissors
        if (hasScissors == True):
            print("You already have scissors.\n")
        # check if user has enough money
        elif (money >= 5):
            money -= 5             # subtract scissor cost
            hasScissors = True     # user has scissors now
            print("You bought a pair of scissors! Now you can cut lawns with them.\n")
        else:
            print("Not enough money. Cut more lawns!\n")
    
    if (user_choice == "3"):
        # check if user has scissors
        if (hasScissors == True):
            money += 5
            print(f"You cut lawns with scissors and earned $5! Total money: ${money}\n")
        else:
            print("You don't have scissors yet. Buy a pair first!\n")
            
    if (user_choice == "4"):
        # check if user alread has lawnmower
        if (hasPushLawnMower == True):
            print("You already have a push lawnmower.\n")
        # check if user has enough money
        elif (money >= 25):
            money -= 25
            hasPushLawnMower = True
            print("You bought a push lawnmower! Now you can cut lawns with it.\n")
        else:
            print("Not enough money. Cut more lawns!\n")
            
    if (user_choice == "5"):
        # check if user has lawnmower
        if (hasPushLawnMower == True):
            money += 50
            print(f"You cut lawns with the push lawnmower and earned $50! Total money: ${money}\n")
        else:
            print("You don't have a push lawnmower yet. Buy one first!\n")
            
    if (user_choice == "6"):
        # check if user has it already
        if (hasBatPowLawnMower == True):
            print("You already have a battery-powered lawnmower.\n")
        # check if user has enough money
        elif (money >= 250):
            money -= 250
            hasBatPowLawnMower = True
            print("You bought a battery-powered lawnmower! Now you can cut lawns with it.\n")
        else:
            print("Not enough money. Cut more lawns!\n")
            
    if (user_choice == "7"):
        # check if user has lawnmower
        if (hasBatPowLawnMower == True):
            money += 100
            print(f"You cut lawns with the battery-powered lawnmower and earned $100! Total money: ${money}\n")
        else:
            print("You don't have a battery-powered lawnmower yet. Buy one first!\n")
            
    if (user_choice == "8"):
        if (hasTeam == True):
            print("You already have a team of starving students.\n")
        elif (money >= 500):
            money -= 500
            hasTeam = True
            print(f"You hired a team of starving students! Now you can use them to cut lawns for you.\n")
        else:
            print("Not enough money. Cut more lawns!\n")
            
    if (user_choice == "9"):
        #check if user has team
        if (hasTeam == True):
            money += 250
            print(f"You cut lawns with your team of starving students and earned $250! Total money: ${money}\n")
        else: 
            print("You don't have a team of starving students yet. Hire one first!\n")
            
    if (user_choice == "10"):
        print(f"Total money: ${money}\n")
        
        
print(f"Congratulations! You've won the game with a team of starving students and ${money}.")