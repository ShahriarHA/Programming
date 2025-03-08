#!/bin/python3

import math
import os
import random
import re
import sys

class Multiset:
    def __init__(self):
        self.elements = {}

    def add(self, val):
        # Adds one occurrence of val to the multiset
        if val in self.elements:
            self.elements[val] += 1
        else:
            self.elements[val] = 1

    def remove(self, val):
        # Removes one occurrence of val from the multiset, if any
        if val in self.elements:
            if self.elements[val] > 1:
                self.elements[val] -= 1
            else:
                del self.elements[val]
    def __contains__(self, val):
    # Returns True when val is in the multiset, else returns False
        if val in self.elements:
            return True
        else:
            return False
    def __len__(self):
        # Returns the number of elements in the multiset
        return sum(self.elements.values())

if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()