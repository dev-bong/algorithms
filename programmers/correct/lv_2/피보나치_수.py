def solution(n):
    global memo
    memo = { # fibo(1) = 1, fibo(2) = 1
        0 : 0,
        1 : 1
    }

    for i in range(2, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 1234567

    return memo[n]

"""
시도 과정
1. recursion 형태로 함수 만듦
    - 시간 초과
2. recursion + dynamic programing
    - 런타임 에러
    #! recursion 최대 횟수?를 넘어서 에러 난것 같음
3. 위 방법
    - 문제 해결
    #* recursion이 정답은 아니다..!? 너무 recursion으로 풀려는 경향이 있는것 같다.. 함수 콜 최대 횟수를 염두하자
"""