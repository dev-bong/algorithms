def bfs(graph, start, des):
    queue = [start]
    visited = set()

    while queue:
        x, y, dist = queue.pop(0)
        if (x, y) == des: # 목적지 도달하면 거리 리턴
            return dist

        if (x, y) not in visited:
            visited.add((x, y))
            move = [(x-1,y), (x,y-1), (x+1,y), (x,y+1)]

            for mv in move:
                if graph[mv[0]][mv[1]] == 2:
                    queue.append((mv[0], mv[1], dist+1)) # 최단거리를 구해야하기 때문에 거리도 계산

def solution(rectangle, characterX, characterY, itemX, itemY):
    system_size = 102
    xy_system = [[0 for j in range(system_size)] for i in range(system_size)] #51

    # xy좌표계에 점 찍기
    for rec in rectangle:
        x1, y1, x2, y2 = rec
        # 2배로 늘려서 찍기
        x1 = 2*x1
        y1 = 2*y1
        x2 = 2*x2
        y2 = 2*y2
        for x in range(x1, x2+1):
            for y in range(y1, y2+1): # 도형 안쪽까지 다 찍기
                xy_system[x][y] = 1

    for x in range(system_size):
        for y in range(system_size):
            if (xy_system[x][y] == 1
            and 0 in [xy_system[x-1][y], xy_system[x][y-1], xy_system[x+1][y], xy_system[x][y+1], xy_system[x-1][y-1], xy_system[x+1][y+1], xy_system[x-1][y+1], xy_system[x+1][y-1]]
            ):
                xy_system[x][y] = 2

    distance = bfs(xy_system, (characterX*2, characterY*2, 0), (itemX*2, itemY*2))

    return distance//2

"""
! 메인 아이디어
1. 2배율로 늘려서 찍기
    - 그대로 찍으면 ㄷ자 형태 1칸단위 꺾임에서 테두리 따기가 어려움

2. 안쪽도 다채우기
    - 테두리 따기가 훨씬 용이해짐
"""
def print_xy(xy_system, size): # xy_system 배율을 xy 평면처럼 프린트
    for y in range(size-1, -1, -1):
        for x in range(size):
            print(xy_system[x][y], end = " ")
        print("")