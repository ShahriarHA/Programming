from collections import Counter

if __name__ == "__main__":
    _X = int(input())
    _shoeSizeList = list(map(int,input().split()))
    countShoeSize = Counter(_shoeSizeList)
    print(countShoeSize)
    countShoeSize.pop(6)
    print(countShoeSize)
    # _N = int(input())
    # for _ in range(_N):
    #     N_customer = list(map(int,input().strip().split(" ")))
    #     d_shoeSize,shoePrice = N_customer[0],N_customer[1]
        # print(d_shoeSize,shoePrice)
