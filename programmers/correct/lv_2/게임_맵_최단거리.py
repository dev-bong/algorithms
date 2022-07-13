def bfs(maps, i_len, j_len):
    queue = [(0, 0, 0)]
    visited = set([(0, 0)]) # 그냥 list로 했을 때 시간초과

    while queue:
        deq_item = queue.pop(0)

        i, j, dis = deq_item
        # 도착
        if i == i_len and j == j_len:
            return dis + 1

        candidate = []

        for t in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]: # 상하좌우 이동
            i, j = t
            if 0 <= i <= i_len and 0 <= j <= j_len: # map 범위에서 벗어나면 X
                if maps[i][j] == 1: # 해당 블록이 뚫려있을 때
                    candidate.append(t)
        
        for c in candidate:
            if c not in visited:
                queue.append((c[0], c[1], dis + 1))
                visited.add(c)

    return visited


def solution(maps):
    i_len = len(maps) - 1
    j_len = len(maps[0]) - 1

    res = bfs(maps, i_len, j_len)
    if type(set()) == type(res):
        return -1
    else:
        return res

"""
bfs에서 visited를 list로 했을 때는 시간 초과가 남
- 중복되는 요소를 계속 넣게 되고
- 그래서 in 연산 하는데 시간이 많이 걸린거 같음

set으로 바꿨더니 시간 초과 해결
"""