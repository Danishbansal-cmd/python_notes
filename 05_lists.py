import sys

thislist = ['banana','apple','orange','pomegranate','chikoo']
print("thislist",thislist)
#this is called
#using ranges to get the items
#of list, nameOfIterable(start:index)
print(thislist[:2])
print(thislist[2:])

#accessing the list using 
#negative indexing
print(thislist[-2:])

#change the list of items
print("after changing the list of items")
thislist[-2:] = ['tatti','khaloo','firultikardo','letsee']
print("thislist", thislist)

#replacing many items with single item
"""
important note here!!!
item one is replacing must be in array also
not in string quote only
"""
thislist[-4:] = ["hahasingleitemonly"]
print("thislist", thislist)

#inserting at specified index
thislist.insert(3,"newfruit")
#inserting at the last
thislist.append("pineapple")
print("thislist", thislist)

#using extend to add the item in the list
newtuple = ("apple_tuple","banana_tuple")
thislist.extend(newtuple)
newdict = {"fruit1":"apple_dict","fruit2":"banana_dict"}
thislist.extend(newdict)
print("after exteding the dict and tuple in list",thislist)

#deletion method for the array
print("to remove the last item",thislist.pop())
print("to remove the specified item",thislist.pop(6))
print("to remove the specified item",thislist.remove("hahasingleitemonly"))
del thislist[4]
# print("to remove the whole list",thislist.clear())
print("thislist",thislist)
newlistcopy = thislist.copy()
newlistusinglist = list(newlistcopy)
# print(thislist)
newlistcopy.pop()
print("modify the existing list",newlistcopy)
print(newlistusinglist)

# newlistusinglist.clear()
# print(newlistusinglist)

numarr = tuple([x for x in range(20)])
print(type(numarr))
print(max(numarr))