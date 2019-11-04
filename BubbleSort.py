nums = []

def Inputs():
    maxNums = int(input("How many numbers to sort? : "))
    for i in range(maxNums):
        n = int(input("Add number : "))
        if n not in nums: nums.append(n)

def BubbleSort():
    n = len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

def output():
    print(nums)

Inputs()
BubbleSort()
output()
