def average(array):
    # your code goes here
    # print(array)
    # print(set(array))
    thisSet = set(array)
    total = 0
    for x in thisSet:
        total+=x
    avg = total/len(thisSet)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)