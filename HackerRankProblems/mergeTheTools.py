def merge_the_tools(string, k):
    # your code goes here
    # factor = len(string)//k
    # print(factor)
    # subStringList = []
    subString = ""
    i = 0
    while i < len(string):
        # subStringList.append(string[i:i+factor])
        subString = string[i:i+k]
        result = ""
        for char in subString:
            if char not in result:
                result+=char
        print(result)
        # print(subString)
        i+=k
    # print(subStringList)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)