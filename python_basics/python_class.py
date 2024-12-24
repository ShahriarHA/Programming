# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.
class myy_class:
    x = 5
print(myy_class)
class_1 = myy_class()
print(class_1.x)

class person:
    def __init__(self,name,age):
        self.n = name
        self.a = age
    def __str__(self):
        return f"my name is {self.n} and I am {self.a}"
p1 = person("Jhon",34)
# print(p1.n)
# print(p1.a)
print(p1)

# create a method in the car class:
class Car:
    def __init__(self,wheel,color):
        self.w = wheel
        self.c = color
    def is_Car_running(self):
        print(f"{self.w} wheels are running!")

car1 = Car(4,"red")
car1.is_Car_running()




