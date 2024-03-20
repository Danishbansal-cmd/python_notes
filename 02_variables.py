import sys
import random

x = 4
x, y = str(2), str("hi this is me")
z = int(6)
a = float(4)

# print(a)
# print(type(x))
# print(type(y))
# print(type(z))

#unpacking a collection
fruits = ["banana", "apple", "orange"]
banana, apple, orange = fruits
print(banana, apple, orange, "with string value also")

#global variables
global_x = int(56)

def printVariable(param1):
    #to create the local variable a global variable
    global global_y
    global_y = str("awesome")
    global global_x
    global_x = str("hahha")
    print("the value of parameter is",param1)    

printVariable(global_x)
print(global_x)
printVariable(global_y)

#print random
print(random.randrange(1,10))
# toInt = int("asdfasdf")
# print(toInt)