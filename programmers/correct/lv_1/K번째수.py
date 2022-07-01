def execute_command(arr, command):
    i, j, k = command
    arr = arr[i-1: j]
    arr.sort()
    return arr[k-1]

def solution(array, commands):
    answer = []

    for c in commands:
        answer.append(execute_command(array, c))

    return answer