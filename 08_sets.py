import sys
newset = {"apple","banana","orange","cherry","strawberry",False,0}
print("newset",newset)

#can create a set using set() constructor method
setconstructor = set(("hehe","haha","hehehe","orange"))
setconstructor.add("newhehe")
setconstructor.add("apple")

#to add the another set into the current
#use the update() method
# setconstructor.update(newset)
print("setconstructor",setconstructor)
newset.intersection_update(setconstructor)
newset3 = newset.intersection(setconstructor)
print('newset2',newset)
print('newset3',newset3)


