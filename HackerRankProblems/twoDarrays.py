if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    
    dimensionOfA = len(arr)
    subSetADim = 3
    mulOFSubA = []
    for i in range(dimensionOfA):
        if i*subSetADim <= dimensionOfA:
            mulOFSubA.append(i*subSetADim)
    print(mulOFSubA)

    # main work
    arr2=[]
    len_mulOFSubA = len(mulOFSubA)
    for s in range(len_mulOFSubA):
        # print(mulOFSubA[s])
        if mulOFSubA[s] == dimensionOfA:
            print("array itteration is done!")
            break
        else:
            # print(mulOFSubA[s])
            for k in range(dimensionOfA):
                sumation = 0
                j = k
                arr3=[]
                while(j < subSetADim+k):
                    i = mulOFSubA[s]
                    while(i < mulOFSubA[s+1]):
                        print(arr[j][i])
                        # arr3.append(arr[j][1])
                        i+=1
                    j+=1
                arr2.append(arr3)

    print(arr2)




