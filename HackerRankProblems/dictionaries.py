if __name__ == "__main__":
    n = int(input())
    phoneBook = dict()
    for _ in range(n):
        keys_vlaues = list(map(str,input().split()))
        # print(keys_vlaues[0])
        # print(keys_vlaues[1])
        phoneBook.update({keys_vlaues[0]:keys_vlaues[1]})
    # print(phoneBook)
    queries = list(input())
    # for x,y in phoneBook.items():
    #     # queries = input().strip()
    #     if queries == "":
    #         print("berak")
    #         break
    #     else:
    #         # print(f"{x} = {y}")
    #         if queries == x:
    #             print(f"{x}={y}")
    #         else:
    #             print("Not found")





