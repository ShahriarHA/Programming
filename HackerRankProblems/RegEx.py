import re
# a = "hello"
# con = re.search("[a-z]",a).string
# print(con)

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    nameList = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        firstNameRe = re.match(r"^[a-z]+$", firstName)
        emailIDRe = re.match(r"^[a-z.]+@gmail\.com$", emailID)
        if firstNameRe==None or emailIDRe==None:
            continue
        else:
            if (firstName==firstNameRe.string) and (emailID==emailIDRe.string): nameList.append(firstName)
        # print(firstNameRe.string,emailIDRe.string)
    # print(nameList)
    nameList.sort()
    for name in nameList:
        print(name)
        

