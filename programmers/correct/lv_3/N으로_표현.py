def only_n(num, n): # 숫자 num의 모든 자리수가 n인지 검사
    str_n = str(num)
    one = str(n) * len(str_n)
    if str_n == one:
        return True
    else:
        return False

def n_expression(n, k):
    # n을 k번 사용하여 얻을 수 있는 숫자들 집합을 리턴
    # k : n을 사용한 횟수 (최대 8)
    if k in memo:
        return memo[k]
    else:
        memo[k] = set() # 이 위치가 맞음
        for i in range(1, k):
            front = n_expression(n, i)
            rear = n_expression(n, k - i)

            #! 원래 memo[k] = set() 위치
            for f in front:
                for r in rear:
                    cand = [f + r, f - r, f * r]
                    if r != 0:
                        cand.append(f // r)
                    if only_n(f, n) and only_n(r, n):
                        cand.append((f * (10 ** len(str(n)))) + r)
                    
                    memo[k].update(cand)
                    
        return memo[k]


def solution(N, number):
    global memo
    memo = {1 : set([N])}

    for i in range(1, 9): # k 최대값은 8이므로 8까지만
        res = n_expression(N, i)
        if number in res: # 끝까지 가기전에 number 완성하면 리턴
            return i

    return -1 # k=8 일때까지 못찾으면 -1

"""
#! memo[k] = set()를 #! 위치에 두어서 실패했었음
예를들어 k가 3일 때..
원래 위치에 두면 i = 1 일 때 memo[k] 업데이트 해놓고
i = 2 일 때 memo[k] 를 다시 초기화 하게 됨...

초기화 타이밍에 주의하자!!!
"""