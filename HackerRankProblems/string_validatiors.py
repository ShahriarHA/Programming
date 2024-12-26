def alphanumeric(s):
    cout = 0
    temp = "False"
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= '0' and s[i] <= '9'):
            cout+=1
    if cout > 0:
        temp = "True"
    return temp
def alphabetic(s):
    cout = 0
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            cout+=1
    return cout
def isdigits(s):
    cout = 0
    temp = "False"
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            cout+=1
    if cout > 0:
        temp = "True"
    return temp
def islowercase(s):
    cout = 0
    temp = "False"
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z'):
            cout+=1
    if cout > 0:
        temp = "True"
    return temp
def isuppercase(s):
    cout = 0
    temp = "False"
    for i in range(len(s)):
        if (s[i] >= 'A' and s[i] <= 'Z'):
            cout+=1
    if cout > 0:
        temp = "True"
    return temp
if __name__ == '__main__':
    s = input()
    alnumeric = alphanumeric(s)
    print(alnumeric)
    alpbe = alphabetic(s)
    if alpbe>0:
        print("True")
    else:
        print("False")
    digits = isdigits(s)
    print(digits)
    lowercase = islowercase(s)
    print(lowercase)
    uppercase = isuppercase(s)
    print(uppercase)

    
    