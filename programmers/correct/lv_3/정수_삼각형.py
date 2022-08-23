def route_max_sum(triangle, cur):
    # (0, 0)에서 현재 위치까지 경로들 중 최대 숫자 합
    cur_h, cur_x = cur
    if cur_x < 0 or cur_x > cur_h: # 여기에 조건을 넣어서 아래 else문을 단순화 (아래 코드와 비교해서)
        return 0

    if cur in memo: # memo에 기록된 것 이용
        return memo[cur]
    else: # memo에 없으면 새로 기록
        memo[cur] = triangle[cur_h][cur_x] + max([route_max_sum(triangle, (cur_h - 1, cur_x)), route_max_sum(triangle, (cur_h - 1, cur_x - 1))])
        return memo[cur]

def solution(triangle):
    height = len(triangle)
    global memo
    memo = {(0, 0) : triangle[0][0]} # 다이나믹 프로그래밍을 위한 memo 딕셔너리 + 초기값 넣어주기
    res = []

    for i in range(height): # 삼각형 맨 아래 라인 좌표들의 최대값 구하기
        res.append(route_max_sum(triangle, (height - 1, i)))

    return max(res) # 최대값 중 최대값

"""
#! No 다이나믹 프로그래밍, No memoization
def route_max_sum(triangle, cur):
    cur_h, cur_x = cur
    if cur_h == 0:
        return triangle[0][0]
    else:
        if cur_x == 0:
            return triangle[cur_h][cur_x] + route_max_sum(triangle, (cur_h - 1, cur_x))
        elif cur_x == cur_h:
            return triangle[cur_h][cur_x] + route_max_sum(triangle, (cur_h - 1, cur_x - 1))
        else:
            return triangle[cur_h][cur_x] + max([route_max_sum(triangle, (cur_h - 1, cur_x)), route_max_sum(triangle, (cur_h - 1, cur_x - 1))])
"""