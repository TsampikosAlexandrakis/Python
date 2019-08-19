import random,time

number = [1,2,3,4,5,6]
active = True

def Roll():
    active == False
    answer = input("Would you like to roll again? Press Y/N ")
    dice = random.choice(number)
    if answer == "Y" or answer == "y":
        print("Rolling . . .")
        time.sleep(1)
        print(dice)
        active == True
    elif answer == "N" or answer =="n":
        print("Quiting...")
        time.sleep(1)
        quit()
    else:
        print("ERROR: Unkown Character")
        active==True 
    
answer = input("Would you like to roll the Dice? Press Y to roll OR N to Quit ")
if answer == "Y" or answer == "y":
    dice = random.choice(number)
    print("Rolling . . .")
    time.sleep(1)
    print(dice)
    active == True
elif answer == "N" or answer =="n":
    quit()
else:
    print("ERROR: Unkown Character")
    active == True

while active == True:
    Roll()
