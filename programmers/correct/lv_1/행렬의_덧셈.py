def arr_size(arr):
    a = len(arr)
    b = len(arr[0])
    return (a, b)

def solution(arr1, arr2):
    answer = [[]]
    a, b = arr_size(arr1)
    answer = [[0 for j in range(b)] for i in range(a)]

    for i in range(a):
        for j in range(b):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer