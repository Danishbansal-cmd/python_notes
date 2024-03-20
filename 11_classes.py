class newClass:
    x = int(345)

obj1 = newClass()
print(obj1.x)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"My name is {self.name} and the age is({self.age})"

p1 = person("potti",45)
print(p1.name)
print(p1.age)
print(p1)

#call the "self" keyword anything but it has
#to be the first keyword for the function
class thing:
    def __init__(hehe,name) -> None:
        hehe.name = name
    def __str__(hoho) -> str:
        return f"My name is {hoho.name}"
thing1 = thing("chootaaa")
print("this is thing1",thing1)

#if one has nothing for the class statement
#one can use pass statement
class monkey:
    pass

class student(person):
    def __init__(self, name, age):
        person.__init__(self,name, age)
        #or can also use this
        # super().__init__(name, age)

stu1 = student("danish",22)
print(stu1)
