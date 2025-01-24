from itertools import permutations

if __name__ == "__main__":
    inputList = list(map(str,input().split(" ")))
    s,k = inputList[0],int(inputList[1])
    sortedS = "".join(sorted(s))
    permutationList = permutations(sortedS,k)
    for j in permutationList:
        (t1,*t2) = j
        words = ""
        for i in t2:
            words+=i
        print(f"{t1}{words}")



