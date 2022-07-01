def gcd(n,m): # 최대공약수
    lower, bigger = (n,m) if n < m else (m,n)
    lower_divisor = []
    res = 0

    for i in range(lower, 0, -1): # 작은 수의 약수들
        if lower % i == 0:
            lower_divisor.append(i)
    
    for ld in lower_divisor:
        if bigger % ld == 0:
            return ld


def lcm(n,m): # 최소공배수
    lower, bigger = (n,m) if n < m else (m,n)

    i = 1
    while True:
        mul = bigger * i # 큰 수의 배수
        if mul % lower == 0:
            return mul
        i += 1

def solution(n, m):
    g = gcd(n,m)
    l = lcm(n,m)
    return [g, l]
# TODO : 인수분해로 풀어보기??