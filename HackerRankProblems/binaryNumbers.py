if __name__ == '__main__':
    n = int(input().strip())
    binaryOfN = format(n,'b')
    # print(binaryOfN)
    count1 = 0
    maxNumber = []
    for i in binaryOfN:
        # print(i)
        if i == "1":
            count1 += 1
        elif i == "0":
            maxNumber.append(count1)
            count1 = 0
    maxNumber.append(count1)
    print(max(maxNumber))

