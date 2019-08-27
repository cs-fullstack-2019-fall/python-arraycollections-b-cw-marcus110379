# Create a function with the variable below. After you create the variable do the instructions below that.
# # ```
# # arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
# b) Print the size of the array
# c) Delete the second element.
# d) Print the 3rd element.
def problem1():
    variableBelow()
def variableBelow():
    arrayForProblem1 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem1[2])
    print(len(arrayForProblem1))
    arrayForProblem1.remove("Kevin")
    print(arrayForProblem1[2])
problem1()

## Problem 2:
##### We will keep having this problem until EVERYONE gets it right without help
#Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def loop():
    userInput = input("enter a string ")
    while userInput != "q" : # if userinput is not equal to "q" loop continues
        userInput = input("enter another string ")
loop()

# Problem 4:
#Create an array of 5 numbers. <strong>Using a loop</strong>, print the elements in the array reverse order. <strong>Do not use a function</strong>
numList = [] # !! : this array is empty
for eachElement in range(5): # !! : you should be altering you range 
    numList.append(eachElement)
    print(numList[:: -1]) # !! : wrong 

## Problem 5:
# Create a function that will have a hard coded array then ask the user for a number. Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def problem5():
    higher = 0
    numbers = [1,5,20, 40, 50]
    userInput = int(input("enter a number"))
    for eachElement in numbers:
        if userInput > numbers[0]: # !! : you are only checking the value of the first array in the item
            higher = higher +1
            print( str(higher) + " higher") # !! : your printing this for every iteration 
        elif userInput < numbers[0]:
            print("lower")
        else:
            print("equal to")
problem5()


