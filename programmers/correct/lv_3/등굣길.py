def route_num(a, b):
    # (a, b) 까지 도달하는 경로 개수
    if (a, b) in memo:
        return memo[(a, b)]
    elif a < 1 or b < 1:
        memo[(a, b)] = 0
        return memo[(a, b)]
    else:
        memo[(a, b)] = route_num(a - 1, b) + route_num(a, b - 1) # 왼쪽에서 오는 경로 개수 + 위쪽에서 오는 경로 개수
        return memo[(a, b)]
    

def solution(m, n, puddles):
    # 학생은 (1, 1)에서 시작해서 오른쪽 또는 아래쪽으로만 이동 가능
    global memo
    memo = {(1, 1) : 1} # (1, 1)부터 시작

    for puddle in puddles: # 웅덩이 있는 곳은 0 으로 초기화
        memo[(puddle[0], puddle[1])] = 0

    answer = route_num(m, n)

    return answer % 1000000007