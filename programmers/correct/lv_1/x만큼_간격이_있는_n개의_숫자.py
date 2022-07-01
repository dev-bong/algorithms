def solution(x, n):
    answer = []
    ceil = x*n+1 if x > 0 else x*n-1

    if x == 0: # x가 0인 경우, 0을 n개 리턴
        answer = [0] * n
        return answer

    for i in range(x, ceil, x):
        answer.append(i)
    return answer