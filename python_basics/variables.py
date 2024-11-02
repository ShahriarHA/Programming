# many values to multiple variables
x,y,z = 10,20,30
print(x)
print(y)
print(z)

# one value to multiple variables
a = b = c = "orange"
print(a)
print(b)
print(c)

# unpack a collection
print("unpacking a collection")
Fruits = ["banana","apple","cherry"]
f1,f2,f3 = Fruits
print(f1)
print(f2)
print(f3)

# global variable
g1 = "awesome"
def global_function():
    g1 = "fantastic"
    print("python is "+ g1)
global_function()
print("python is "+ g1)
