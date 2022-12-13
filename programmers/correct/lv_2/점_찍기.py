def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        y = int((d**2 - x**2) ** 0.5)
        answer += (y // k) + 1

    return answer

"""
#* 원의 방정식 이용
> x**2 + y**2 = d**2 원의 1사분면에 있는 정수 좌표의 개수를 구하는 문제
"""