# syntex--
# lambda arguments: expression
x = lambda a:a+10
print(x(1))

# Lambda functions can take any number of arguments:
y = lambda a,b,c : a+b+c
print(y(1,2,4))

def myFunction(n):
    return lambda a: a*n
doubleNum = myFunction(2)
print(doubleNum(11))

# Use lambda functions when an anonymous function is required for a short period of time.



