def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def solution(n):
    answer = 0
    cases = []

    # (1 * a) + (2 * b) = n 을 만족하는 a, b 찾기
    for i in range(n+1):
        remain = n - i
        if remain % 2 == 0:
            cases.append((i, remain // 2))
    
    for case in cases:
        a, b = case
        # 1이 a개, 2가 b개인 경우, 그것들을 나열하는 경우의 수 계산
        if 0 in [a, b]: # a, b 둘중 하나가 0이면 경우의 수는 1
            answer += 1
        else: # 경우의 수 = (a + b)!/a!b!
            answer += factorial(a + b)//(factorial(a) * factorial(b))

    return answer % 1234567


##### DP 버전 #####
def solution(n):
    dp = [0 for i in range(2000 + 1)] # 문제에서 제시한 최대 n = 2000
    dp[1] = 1 # (1)
    dp[2] = 2 # (1, 1), (2)

    if n > 2:
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567

"""
A(n) : n칸을 조건에 맞게 뛰는 경우의 수
    조건 : 1칸 또는 2칸씩 뛰어서 목적지에 도착

>> A(n) = A(n - 1) + A(n - 2)
    A(n - 1)에서 한칸 뛰기 + A(n - 2)에서 2칸 뛰기
"""