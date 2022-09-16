import sys
sys.setrecursionlimit(30000) # 최대 recursion depth? 늘리기

def factorial(num):
    if num not in memo:
        memo[num] = num * factorial(num - 1)
    return memo[num]

def solution(n):
    if n == 1:
        return 1
    
    answer = 0
    in_2 = n // 2 # n에 2가 몇개 들어갈수 있는지
    global memo
    memo = {
        0 : 1,
        1 : 1
    }

    #for two in range(in_2 + 1):
    for two in range(in_2, -1, -1):
        one = n - (two * 2)
        if two == 0 or one == 0:
            answer += 1
            continue
        answer += factorial(two + one) // (factorial(two) * factorial(one))
    return answer % 1000000007

#! 정확성 테스트는 모두 통과. 하지만 효율성테스트 통과 X