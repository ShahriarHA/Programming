s = ['1', '2', '3', '4']
result = map(int,s)
# print(result)
# print(list(result))

# syntax of the map function
# map(function,iterable)
a = [1,2,3,4,5]
b = [5,4,3,2,1]
def double(val,val1):
    return val+val1
res1 = map(double,a,b)
# print(list(res1))

# map() with lambda
res2 = list(map(lambda x: x*2,a))
# print(res2)

res3 = list(map(lambda x,y:x+y,a,b))
# print(res3)

# an example
fruits = ['apple', 'banana', 'cherry']
res4 = list(map(str.upper,fruits))
# print(res4)

# Extracting first character from strings
FirstChar = list(map((lambda x:x[0]),fruits))
print(FirstChar)


