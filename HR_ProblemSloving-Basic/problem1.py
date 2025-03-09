#!/bin/python3

import os
from collections import Counter

def stringAnagram(dictionary, query):
    anagram_map = {}
    
    for word in dictionary:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word] = anagram_map.get(sorted_word, 0) + 1
    result = []
    
    for word in query:
        sorted_word = ''.join(sorted(word))  
        result.append(anagram_map.get(sorted_word, 0)) 
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = [input().strip() for _ in range(dictionary_count)]

    query_count = int(input().strip())

    query = [input().strip() for _ in range(query_count)]

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)) + '\n')

    fptr.close()
