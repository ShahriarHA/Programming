if __name__ == '__main__':
    N = int(input())
    lists = []
    for _ in range(N):
        commands = input().split()
        if commands[0] == "insert":
            lists.insert(int(commands[1]),int(commands[2]))
        elif commands[0] == "print":
            print(lists)
        elif commands[0] == "remove":
            lists.remove(int(commands[1]))
        elif commands[0] == "append":
            lists.append(int(commands[1]))
        elif commands[0] == "sort":
            lists.sort()
        elif commands[0] == "pop":
            lists.pop()
        elif commands[0] == "reverse":
            lists.reverse()
    # print(lists)


