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
    print(FinalAlphaSequ)
    centerRangoli = FinalAlphaSequ.replace(" ","-")
    print(centerRangoli)




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)