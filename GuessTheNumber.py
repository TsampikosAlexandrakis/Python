import random,time

number_list = [1,2,3,4,5,6,7,8,9,10]

active = True

random_number = random.choice(number_list)

number = int(input("From 1 to 10 what number am I thinking?"))
if number == random_number:
    print("Correct! I was thinking of :",number)
    active == True
else:
    print("Wrong! It was : ",random_number)
    active == True

while active == True:
    active == False
    random_number = random.choice(number_list)
    number = int(input("From 1 to 10 what number am I thinking?"))
    if number == random_number:
        print("Correct! I was thinking of :",number)
        active == True
    else:
        print("Wrong! It was : ",random_number)
        active == True
