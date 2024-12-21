def count_substring(string, sub_string):
    c = 0
    length_of_sub_string = len(sub_string)
    for i in range(0, len(string)):
        # print(string[i:length_of_sub_string+i])
        if sub_string in string[i:length_of_sub_string+i]:
            c = c+1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)