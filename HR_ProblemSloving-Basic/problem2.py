import os
def findSubstring(s, k):
    vowels = set("aeiou")
    maxVC = 0
    maxVSubS = "Not found!"

    vowelC = sum(1 for l in s[:k] if l in vowels)

    if vowelC > maxVC:
        maxVC = vowelC
        maxVSubS = s[:k]
    for i in range(1, len(s) - k + 1):
        if s[i - 1] in vowels:  
            vowelC -= 1
        if s[i + k - 1] in vowels:  
            vowelC += 1
        
        if vowelC > maxVC:
            maxVC = vowelC
            maxVSubS = s[i:i + k]

    return maxVSubS
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()
    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()