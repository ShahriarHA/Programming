if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # print(student_marks)
    query_name = input()
    sum = 0
    for i in student_marks.keys():
        # print(i)
        if i == query_name:
            # print(student_marks[i][0])
            for j in student_marks[i]:
                # print(j)
                sum = sum + j
    print(f"{sum/3:.2f}")




