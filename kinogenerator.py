import random,time

nums=[]

def gen():
    play_num = 0
    print("Με πόσα νούμερα θέλεις να παίξεις;")
    play_num = int(input())
    if play_num>=1 and play_num<=12:
        for i in range(play_num):
            r = random.randint(0,80)
            if r not in nums: nums.append(r)
        print(nums)
        print("Θέλεις να ξαναπαόξεις; Υ/Ν")
        answer = str(input())
        if answer == "Y" or answer == "y":
            gen()
        elif answer == "N" or "n":
            exit() 
    else:
        print("Λαθος αριθμος! 1-12 ΜΟΝΟ!")
        gen()

gen()
