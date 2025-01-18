import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    # Write your code here
    def pushCharacter(self,a):
        # pass
        self.stack.append(a)
    def enqueueCharacter(self,b):
        # pass
        self.queue.append(b)
    def popCharacter(self):
        # pass
        return self.stack.pop()
    def dequeueCharacter(self):
        # pass
        return self.queue.pop(0)
    def printQS(self):
        print(self.queue)
        print(self.stack)



# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
# obj.printQS()
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    