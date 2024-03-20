import sys
atuple = ("banana","apple","orange","pineapple")
tupleconstructor = tuple(("banana","apple","orange","pineapple"))

tuplewithsinglevalue = ("haha",)
print("tuplewithsinglevalue with value",tuplewithsinglevalue, type(tuplewithsinglevalue))

#as tuples are unchangeable we
#can convert them into list
#and then change it and convert
#back into tuple

y = list(atuple)
y[2] = "newfruit"
atuple = tuple(y)
print("atuple value and type",atuple,type(atuple))

#one can delete tuple using del keyword
del atuple
print("tupleconstructor value, type and length", tupleconstructor, type(tupleconstructor), len(tupleconstructor))
# print(atuple)

# to multiply the contents of the tuple
tuplewithsinglevalue = tuplewithsinglevalue * 4
print(tuplewithsinglevalue)