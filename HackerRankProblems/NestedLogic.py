def checkFine(rdate,dDate):
    d1,m1,y1 = int(rdate[0]),int(rdate[1]),int(rdate[2])
    # print(d1,m1,y1)
    d2,m2,y2 = int(dDate[0]),int(dDate[1]),int(dDate[2])

    if ((d1 <= d2) and (m1 <= m2) and (y1 <= y2)) or ((d1 > d2) and (m1 > m2) and (y1 < y2)):
        return 0
    elif (d1 > d2) and (m1 == m2) and (y1 == y2):
        return (15 * (d1 - d2))
    elif (m1 > m2) and (y1 == y2):
        return (500 * (m1 - m2))
    else:
        return 10000


if __name__ == "__main__":
    returnedDate = input().split(" ")
    # print(returnedDate)
    DueDate = input().split(" ")

    print(checkFine(returnedDate,DueDate))
