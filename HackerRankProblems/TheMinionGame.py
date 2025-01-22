def minion_game(string):
    # your code goes here
    # print(string)
    # vowelsList = []
    # consonentList = []
    KevinPoint = 0
    StuartPoint = 0
    for v in range(len(string)):
        if string[v]=="A" or string[v]=="E" or string[v]=="I" or string[v]=="O" or string[v]=="U":
            # vowelsList.append(v)
            KevinPoint+= len(string) - v

        else:
            StuartPoint+= len(string) - v
            # consonentList.append(v)
    # print(f"Vowel list: {vowelsList}")
    # print(f"Consonent List: {consonentList}")
    
    # for i in vowelsList:
    #     for j in range(i,len(string)):
    #         KevinPoint+=1
    # print(f"Kevin {KevinPoint}")
    # for i in consonentList:
    #     for j in range(i,len(string)):
    #         StuartPoint+=1
    # print(f"Stuart {StuartPoint}")
    if StuartPoint > KevinPoint:
        print(f"Stuart {StuartPoint}")
    elif StuartPoint == KevinPoint:
        print("Draw")
    else:
        print(f"Kevin {KevinPoint}")

if __name__ == '__main__':
    s = input()
    minion_game(s)