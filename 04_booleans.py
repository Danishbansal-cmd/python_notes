import sys

a = int(5)
b = int(10)

if a > b:
    print("a:",a," is greater than b:",b)
else:
    print("b:",b," is greater than a:",a)

#lets see what bool value gives us of different values
print("a number greater than 0",bool(3456))
print("a float",bool(3456.3456))
print("a boolean of true",bool(True))
print("a boolean of false",bool(False))
print("a number equivalent to 0",bool(0))
print("condition",bool(4 > 6))
print("a string",bool("sdfgd"))
print("a empty string",bool(""))
print("list of numbers",bool([3,4.6,547.5,456]))
print("a tuple of numbers",bool(tuple((453,345,345))))
print("a empty tuple",bool(tuple()))
print("a empty list",bool([]))
print("a dictionary",bool({"hi":"hello","potti":"kardo"}))
print("a empty dictionary",bool({}))
print("a range",bool(range(3)))
print("And ofcourse the value None, gives",bool(None))

#use of isinstance method
x = int(345.345)
print(isinstance(x, int))
print(isinstance(x, float))