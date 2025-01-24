from collections import Counter

if __name__ == "__main__":
    _X = int(input())
    _shoeSizeList = list(map(int,input().split()))
    countShoeSize = Counter(_shoeSizeList)
    # elements = list(countShoeSize.elements())
    keys = countShoeSize.keys()
    values = list(countShoeSize.values())
    print(keys,values)
    _N = int(input())
    totalPrice = 0
    for _ in range(_N):
        N_customer = list(map(int,input().strip().split(" ")))
        d_shoeSize,shoePrice = N_customer[0],N_customer[1]
        for i,item in enumerate(keys):
            if d_shoeSize == item and values[i]>0:
                # print("yes")
                values[i]-=1
                totalPrice+=shoePrice
    print(values)
    print(totalPrice)
    # print(elements)
    # totalPrice = 0
    # 
    # for _ in range(_N):
    #     
    #     # print(d_shoeSize,shoePrice)
        
    #     for item in elements:
    #         if d_shoeSize == item:
    #             totalPrice+=shoePrice
    #             elements.remove(item)
    # print(totalPrice)

