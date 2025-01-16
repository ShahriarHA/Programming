#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s1 = s.split(" ")
    # print(s1)
    FullName = ""
    for i in s1:
        # print(i.capitalize())
        FullName+=i.capitalize()+" "
    print(FullName)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
