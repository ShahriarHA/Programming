x = int(input())
y = int(input())
z = int(input())
n = int(input())

list1 = []

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            # print(i,j,k)
            list2 = []
            sum = 0
            list2.append(i)
            list2.append(j)
            list2.append(k)
            sum = i+j+k
            if sum != n:
                list1.append(list2)
print(list1)



