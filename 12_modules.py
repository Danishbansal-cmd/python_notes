import mymodule as mm
from mymodule import person1
#these are built-in modules
import platform

print(platform.system())
print(dir(platform))
print(dir(mm))

obj1 = mm.haha()

print(person1["name"])