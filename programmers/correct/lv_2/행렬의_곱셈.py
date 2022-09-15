def solution(arr1, arr2):
    # col1 == row2 (곱셈 가능한 행렬만 주어진다 했으므로)
    row1 = len(arr1)
    col1 = len(arr1[0])
    col2 = len(arr2[0])
    answer = [[0] * col2 for i in range(row1)]

    for i in range(row1):
        for j in range(col2):
            tmp = 0
            for k in range(col1):
                tmp += arr1[i][k] * arr2[k][j]
            answer[i][j] = tmp

    return answer