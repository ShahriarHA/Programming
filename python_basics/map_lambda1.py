# Write a Python program to triple all numbers in a given list of integers. Use Python map.

num = [1,2,3,4,5]

def tripleNum(n):
    return n*3

numbersT = list(map(tripleNum,num))
print(f"Before using map function: {num}")
print(f"after using map function: {numbersT}")

# using lambda function

result = list(map(lambda a:a*3,num))
print(f"after using lambda function: {result}")




