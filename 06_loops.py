fruitslist = ['Banana','apple','Orange','pomegranate','chikoo']
# for x in range(len(fruitslist)):
#     print(fruitslist[x])

#while loop
i = int(0)
# while i < len(fruitslist):
#     print(fruitslist[i])
#     i = i + 1

"""
this is called looping through list using
list comprehension
"""
# [print(x) for x in fruitslist]
# [print(fruitslist[x]) for x in range(len(fruitslist))]


"""
creating new list using
list comprehension
"""
newlist = [x for x in fruitslist if "a" in x]
# print("this is the newlist",newlist)

newArrayList = [x for x in range(20)]
# print("this is arraylist",newArrayList)

#by default sort is case sensitive and results in
#all capital letters sorter before lower letters
newlist.sort()
print("sorted array",newlist)

#to avoid sorting from case sensitive
#use one of the following
newlist.sort(key = str.lower)
print("this is sorted array without case sensitive",newlist)

newlist.sort(reverse=True)
print("sorted array with reverse order",newlist)

for x in range(0,31,3):
    if x > 18:
        break
    print("value of x is",x)
else:
    print("finally finished")

#if one has no content to pass in the for loop
#one can use pass statement or keyword in the 
#for loop
for x in range(10):
    pass