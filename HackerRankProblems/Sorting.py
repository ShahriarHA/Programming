# a,b = 10, 20
# print(a,b)
# b,a = a,b
# print(a,b)
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    totalSwaps = 0
    for i in range(n):
        numberOfSwaps = 0
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                numberOfSwaps+=1
        totalSwaps+=numberOfSwaps
        if numberOfSwaps == 0:
            break
    # print(a,totalSwaps)
    print(f"Array is sorted in {totalSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")

