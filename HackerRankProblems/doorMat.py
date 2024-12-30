import sys

if __name__ == '__main__':
    matSizeInput = sys.stdin.readline().split()
    n = int(matSizeInput[0])
    m = int(matSizeInput[1])

    designPattern1 = "-"
    designPattern2 = ".|."
    midOfDesignPattern = (m-len(designPattern2))//2
    # print(midOfDesignPattern)
    # print(n//2)

    DesignPattern2List = []
    designPattern = ""
    for i in range(0, n//2):
        if i >= 1:
            designPattern = designPattern + designPattern2 + designPattern2
        else:
            designPattern += designPattern2
        DesignPattern2List.append(designPattern)
    # print(DesignPattern2List)

    finalDesignPatternList = []
    for _ in range(0,n//2):
        des1 = ""
        for _ in range(0,m):
            des1 += designPattern1
        finalDesignPatternList.append(des1)
    # print(finalDesignPatternList)
    # print(len(finalDesignPatternList[0]))

    fList = []
    for x in DesignPattern2List:
        for y in finalDesignPatternList:
            midString = y[:midOfDesignPattern]
            y = midString + x + midString
        # print(y,len(y))
        fList.append(y)
        midOfDesignPattern -= 3

    # print(finalDesignPatternList)
    # print(fList)
    message = "WELCOME"
    messageLen = len(message)
    lenFDPL = len(finalDesignPatternList[0])
    centerOfMess = (lenFDPL - messageLen) // 2
    # print(centerOfMess)
    fMessage = finalDesignPatternList[0][:centerOfMess] + message + finalDesignPatternList[0][:centerOfMess]
    # print(fMessage,len(fMessage))
    

    # print(fList)

    fflist = []
    
    for m in fList:
        # print(m)
        fflist.append(m)
    fflist.append(fMessage)

    fList.reverse()
    for a in fList:
        fflist.append(a)
    
    print("------printin final list--------")
    for f in fflist:
        print(f)


