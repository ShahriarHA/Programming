# Write a Python program to add three given lists using Python map and lambda.

a,b,c = [1,2,3],[4,5,6],[7,8,9]
# print(a,b,c)
# def addThreeMap(a,b,c):
#     finallist = []
#     finallist.extend(a)
#     finallist.extend(b)
#     finallist.extend(c)
#     return finallist
res1 = list(map(lambda a,b,c:a+b+c,a,b,c))
print(res1)