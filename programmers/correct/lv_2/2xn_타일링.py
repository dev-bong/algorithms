def solution(n):
    memo = [0 for i in range(n + 1)] 
    memo[0] = 1
    memo[1] = 1
    
    for i in range(2, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 1000000007 #! 중요
    
    return memo[n] % 1000000007

"""
피보나치 수열이었음
    A(n)
        1. 처음에 한칸짜리를 놓는 경우 : A(n - 1)
        2. 처음에 두칸짜리를 놓는 경우 : A(n - 2)
    >> A(n) = A(n - 1) + A(n - 2)

큰 수를 연산하는데는 시간이 오래걸린다
#? 저렇게 나누면서 해도 결과가 달라지지 않는듯?
"""