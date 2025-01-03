if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr)
    hourGlassArr = []
    dimesionOfArr = len(arr)
    for i in range(dimesionOfArr):
        for j in range(dimesionOfArr):
            if (i+2 < dimesionOfArr) and (j+2 < dimesionOfArr):
                hourGlassValue = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                hourGlassArr.append(hourGlassValue)
    # print(hourGlassArr)
    print(max(hourGlassArr))    




