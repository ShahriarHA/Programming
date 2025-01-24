from itertools import product
if __name__ == "__main__":
    a = list(map(int,input().split(" ")))
    b = list(map(int,input().split(" ")))
    # print(a,b)
    a.sort()
    b.sort()

    result = list(product(a,b))
    print(*result)
    # print(" ".join(map(str,result)))


