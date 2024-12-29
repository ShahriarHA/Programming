import sys

if __name__ == '__main__':
    matSizeInput = sys.stdin.readline().split()
    n = int(matSizeInput[0])
    m = int(matSizeInput[1])
    # print(n,m)
    # print(type(n))
    designPattern1 = "-"
    designPattern2 = ".|."
    midOfDesignPattern = (m-len(designPattern2))//2
    print(midOfDesignPattern)
    print(n//2)
    # print(len(designPattern2))
    # for _ in range(0,(n//2)+1):
    #     designPattern = ""
    #     for i in range(0,(m-len(designPattern2)+1)):
    #         if i == midOfDesignPattern:
    #             designPattern = designPattern + designPattern2
    #         else:
    #             designPattern = designPattern + designPattern1
    #     print(designPattern)
    # print(len(designPattern))
    DesignPattern2List = []
    designPattern = ""
    for i in range(0, n//2):
        if i >= 1:
            designPattern = designPattern + designPattern2 + designPattern2
        else:
            designPattern += designPattern2
        DesignPattern2List.append(designPattern)
    print(DesignPattern2List)

    finalDesignPatternList = []
    for _ in range(0,n//2):
        des1 = ""
        for _ in range(0,m):
            des1 += designPattern1
        finalDesignPatternList.append(des1)
    print(finalDesignPatternList)
    print(len(finalDesignPatternList[0]))

    print("---main work---")

    for j in range(0,len(finalDesignPatternList)):
        # print(finalDesignPatternList[j][midOfDesignPattern:midOfDesignPattern+3])
        midStringValue = finalDesignPatternList[j][midOfDesignPattern:midOfDesignPattern+3]
        print(midStringValue,designPattern2)

    print(finalDesignPatternList)




