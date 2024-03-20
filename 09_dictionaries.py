a = {"he":"hello","how":"areyou","whatis":"goingon","patani":True,3:34}
print(a)
print(a[3])
print(a.get(3))

#create set using set() constructor
b = dict(fruit = "apple", he = "2nubmer", ha = "number")


#to get the list of keys
print(b.keys())
for x in b.values():
    print(x)

print(a.items())

#for adding data to dict
a["color"] = "red"
print("a",a)

#another way to add
b.update({"1234":"5678"})
print("b",b)

#removing items
a.pop("he")
print("a",a)


