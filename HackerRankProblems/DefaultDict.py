from collections import defaultdict

if __name__ == "__main__":
    intergers = list(map(int,input().split(" ")))
    n,m = intergers[0],intergers[1]
    Ddict = defaultdict(list)
    for _ in range(n):
        value = input()
        Ddict["A"].append(value)
    for _ in range(m):
        val = input()
        Ddict["B"].append(val)
    
    a,b = Ddict["A"],Ddict["B"]
    # print(a,b)
    for i in b:
        indexList = []
        temp = 0
        for ind,val1 in enumerate(a):
            if val1 == i:
                temp+=1
                indexList.append(ind+1)
        if temp == 0:
            print(-1)
        else:
            print(*indexList)

    

