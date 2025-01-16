def print_rangoli(size):
    # your code goes here
    # totalSize = size+96
    # ascii_char = ""
    # ascii_char = chr(totalSize)
    # print(ascii_char)
    alphabetSequence = ""
    for i in range(1,size+1):
        totalSize = 96
        totalSize += i
        ascii_char = ""
        ascii_char = chr(totalSize)
        # print(ascii_char)
        alphabetSequence += ascii_char + " " if i!=size else ascii_char
    # print(alphabetSequence)
    revAlphaSequence = alphabetSequence[::-1]
    FinalAlphaSequ = revAlphaSequence[:len(revAlphaSequence)-1] + alphabetSequence
    # print(FinalAlphaSequ)
    centerRangoli = FinalAlphaSequ.replace(" ","-")
    # print(centerRangoli)
    midOfCenterRangoli = len(centerRangoli) // 2
    # print(centerRangoli[midOfCenterRangoli])
    listOfRangolies = []
    for i in range(size):
        if i == 0:
            # print(centerRangoli)
            listOfRangolies.append(centerRangoli)
        else:
            x = centerRangoli[midOfCenterRangoli-1:midOfCenterRangoli+3]
            y = centerRangoli.replace(x,"")
            y = "--" + y + "--"
            # print(y)
            listOfRangolies.append(y)
            centerRangoli = y
    listOfRangolies.reverse()
    # print(listOfRangolies)
    for i in listOfRangolies:
        print(i)
        # pass
    listOfRangolies.reverse()
    for j in range(len(listOfRangolies)):
        if j == 0:
            continue
        else:
            print(listOfRangolies[j])





if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)