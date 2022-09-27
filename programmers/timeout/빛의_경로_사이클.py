from collections import deque

def straight(a, b): # a로부터 도착, b를 거쳐 straight하게 도착하는 좌표 리턴
    return (b[0] + (b[0] - a[0]), b[1] + (b[1] - a[1]))

def left(a, b):
    if a[0] == b[0]:
        return (b[0] - (b[1] - a[1]), b[1])
    elif a[1] == b[1]:
        return (b[0], b[1] + (b[0] - a[0]))

def right(a, b):
    if a[0] == b[0]:
        return (b[0] + (b[1] - a[1]), b[1])
    elif a[1] == b[1]:
        return (b[0], b[1] - (b[0] - a[0]))

def move(a, b, ij_grid):
    if ij_grid[b[0]][b[1]] == "S":
        return straight(a, b)
    elif ij_grid[b[0]][b[1]] == "L":
        return left(a, b)
    elif ij_grid[b[0]][b[1]] == "R":
        return right(a, b)
    elif ij_grid[b[0]][b[1]] == "0":
        res = straight(a, b)
    return (res[0] % len(ij_grid), res[1] % len(ij_grid[0]))

def solution(grid):
    answer = []
    grid_idxs = []
    visited = set()
    len_grid = len(grid[0])

    ### ! 이렇게 grid 조작하지 말고 입력으로 온 grid 그대로 쓰는 방법으로..
    grid = deque(grid)
    padding_0 = "0" * (len(grid[0]) + 2)
    grid.append(padding_0)
    grid.appendleft(padding_0)
    for i in range(1, len(grid) - 1):
        grid[i] = "0" + grid[i] + "0"
        grid_idxs.extend([(i, j + 1) for j in range(len_grid)])
    ###

    for g_idx in grid_idxs:
        starts = [(g_idx[0] + 1, g_idx[1]), (g_idx[0] - 1, g_idx[1]), (g_idx[0], g_idx[1] + 1), (g_idx[0], g_idx[1] - 1)]
        for start in starts:
            a = start
            b = g_idx
            st_rt = (start, b)

            if st_rt in visited:
                continue
            else:
                visited.add(st_rt)
            
            idx_history = set([st_rt])
            route_len = 0
            while True:
                nxt = move(a, b, grid)
                next_route = (b, nxt)

                if nxt in grid_idxs:
                    route_len += 1

                if next_route in visited:
                    break
                idx_history.add(next_route)
                visited.add(next_route)

                if next_route == st_rt:
                    break
                a = b
                b = nxt

            if idx_history:
                answer.append(route_len)

    answer.sort()
    return answer

"""
#TODO : 좀 복잡해서 풀다 만 문제.. 이어서 풀어보도록
"""