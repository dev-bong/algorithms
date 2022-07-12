def move(current, arrow): # 규칙에 맞게 좌표 이동
    pattern = [0, 1, 1, 1, 0, -1, -1, -1]
    x = current[0] + pattern[arrow]
    y = current[1] + pattern[(arrow + 2) % 8]

    return (x, y)

def solution(arrows):
    cur_xy = (0, 0)
    next_xy = None
    next_xy2 = None
    visited_vertex = set([cur_xy])
    visited_edge = set()

    for arrow in arrows:
        next_xy = move(cur_xy, arrow)
        visited_vertex.add(next_xy)
        visited_edge.add((cur_xy, next_xy))
        visited_edge.add((next_xy, cur_xy)) # ((1,1),(2,2))와 ((2,2),(1,1))은 같은 선이므로 바꿔서 한번 더넣기

        next_xy2 = move(next_xy, arrow)
        visited_vertex.add(next_xy2)
        visited_edge.add((next_xy, next_xy2))
        visited_edge.add((next_xy2, next_xy))

        cur_xy = next_xy2

    v = len(visited_vertex)
    e = len(visited_edge) // 2 # 바꿔서 하나씩 더 넣어서 개수가 2배이므로 2로 나누기
    print(v, e)
    return 1 - v + e

"""
잘 안풀려서 질문하기에서 오일러 공식(오일러의 다면체 정리) 힌트 얻어서 품
v - e + f = 1 (v : 점의 개수, e : 엣지 개수, f : 면의 개수)

오일러 공식 말고 풀어보기???
"""