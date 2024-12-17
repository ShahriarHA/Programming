if __name__ == '__main__':
    list1 = []
    for N in range(int(input())):
        name = input()
        score = float(input())
        list2 = []
        list2.append(name)
        list2.append(score)
        list1.append(list2)
    print(list1)
    # print(list1[2][1])
    min_value_list = []
    for x in list1:
        # print(x[1])
        min_value_list.append(x[1])
    print(min_value_list)
    min_value_list.sort()
    print(min(min_value_list))
    min_value = min(min_value_list)
    length = len(min_value_list)
    # print(length)
    
    students_name = []
    for i in range(0,length):
        if min_value_list[i] > min_value:
            for j in list1:
                if min_value_list[i] == j[1]:
                    students_name.append(j[0])
            break
    students_name.sort()
    for n in students_name:
        print(n)
        

    