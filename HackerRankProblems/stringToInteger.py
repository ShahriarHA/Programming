#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    S = input().strip()
    print(type(S))
    try:
        intOfS = int(S)
        print(intOfS)
    except:
        print("Bad String")
