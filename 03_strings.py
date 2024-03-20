multilineString = """this is the multiline
string that could be used
either for the comment or variable"""
print(multilineString)

stringArray = "this is array from string"
# print(stringArray[0])
# print(stringArray[4])
print(stringArray[len(stringArray) - 1])

#looping a string
# for x in stringArray:
#     print(x)

#check the string
print("array" in stringArray)

#can be used in if condition
# if "array" in stringArray:
#     print("this is present in array")
# else:
#     print("this is not present in array")

# if "array" not in stringArray:
#     print("this is not present in array")
# else:
#     print("this is present in array")

# print(stringArray[3:len(stringArray)])
# print(stringArray[3:])
# print((stringArray[3:]).upper())

helloWorld = "hello world   "
print(helloWorld.strip())
helloArray = (helloWorld.strip()).split(" ")
print(helloArray)