import math

foo = 50
bar = 50.0

name = "Christian"

print(name)

print(name, foo, bar, sep="", end="")
#default seperator is spaces
#default ends in a newline, but this can be changed

# formatted strings: f-string
print(f"Hi, {name.upper()}.\nThe sum is {foo+bar}.")

# string methods like upper()
x = 3
print(f"x is {x}; x squared is {x**2}; x^2 is {x^2}.")

#name = input("What is your name? ")
#print(f"Bye, {name.lower()}!")

# Need to cast input into an int or float to do math
# number = input("Give me a number: ")
# if number.isnumeric(): # colon starts a code block, like { in C++
#     number = int(number)
#     print(f"The next number is {number + 1}.")
# else:
#     print("HEY! That wasn't a number")
# print("Goodbye!")


# catch errors with try...except
try:
    number = float(input("Give me a number (float): "))
    print(f"The sqrt is {math.sqrt(number)}")
except ValueError:
    print("That Wasn't a number.")

# countdown with a while loop
count = 10
while count > 0:
    print(count)
    count -= 1 #python has no ++ or --
print("Blast off!")

# no do-while in python, need to use while True
while True: # note the capital T.
    response = input("Type q to quit.")
    if response == "q":
        break # takes us out of the while loop

# for loop syntax is very different from C++
# do something 5 times
for i in range(5):
    print("HI!", i) 

# lists
food = ["crab", "steak", "sushi"]
print(food[0]) #"crab"
food[1] = "bananas" #crab, bananas, sushi
print(food)
food.append("chocolate") #crab, bananas, sushi, chocolate
print(food)
food.remove("bananas") #crab, sushi, chocolate
print(food)
food.pop(1) #crab, chocolate
print(food)

# not a copy
food2 = food
# both food2 and food refer to the same list
food.append("Yogurt")
print(food, "\n", food2)

# this does make a copy
food2 = food.copy()
food.append("Hotdog")
print(food, "\n", food2)

for a in food:
    print(a + "s") # + with strings is concatentation

# 2D array = list of lists
array = [] # initial empty list
for i in range(3):
    array.append([]) # new empty list for each row
    for j in range(5):
        array[i].append(f"{i},{j}") # append each element
print(array)

numbers = [i**2 for i in range(5)]
print(numbers)

# list comprehension, faster than regular for loops
array2 = [[ f"{i,j}" for j in range(5)] for i in range(3)]
print(array2)