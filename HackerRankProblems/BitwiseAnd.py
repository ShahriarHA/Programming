#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    # print(N,K)
    # s = []
    # for i in range(1,N+1):
    #     s.append(i)
    # print(s)
    # listOfab = []
    # for j in s:
    #     for m in s:
    #         if j<m:
    #             a_b = j&m
    #             if a_b < K:
    #                 listOfab.append(a_b)
        # b = j+1
        # if b <= N:
        #     result = j&b
        #     if result < K:
        #         listOfab.append(result)
    # print(listOfab)

    # return (K - 1) | K <= N
    if (K - 1) | K <= N:
        return K - 1
    else:
        return K - 2
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)
        print(res)
        # fptr.write(str(res) + '\n')

    # fptr.close()
