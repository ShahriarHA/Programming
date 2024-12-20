if __name__ == '__main__':
    n = int(input())
    arr = list((map(int, input().split())))
    # print(arr)
    arr.sort(reverse=True)
    # print(arr)
    # print(arr[0])
    for i in arr:
        # print(i)
        if i < arr[0]:
            print(i)
            break


