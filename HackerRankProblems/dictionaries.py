import sys

if __name__ == "__main__":
    n = int(input())
    phoneBook = dict()
    for _ in range(n):
        keys_vlaues = list(map(str,input().split()))
        phoneBook.update({keys_vlaues[0]:keys_vlaues[1]})
    queries = sys.stdin.readlines()
    for query in queries:
        # print(f"{query}")
        name = query.strip()
        if name in phoneBook.keys():
            print(f"{name}={phoneBook[name]}")
        else:
            print("Not found")

