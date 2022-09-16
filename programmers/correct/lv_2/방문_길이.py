def move(dirs_list): # dirs_list 대로 좌표 이동
    vtx = [0, 0]
    dir_dict = {
        "U" : [0, 1],
        "L" : [-1, 0],
        "R" : [1, 0],
        "D" : [0, -1]
    }
    vtx_range = [n for n in range(-5, 6)]
    route = [(vtx[0], vtx[1])]

    for d in dirs_list:
        vtx[0] += dir_dict[d][0]
        vtx[1] += dir_dict[d][1]

        if vtx[0] not in vtx_range:
            vtx[0] -= dir_dict[d][0]
        elif vtx[1] not in vtx_range:
            vtx[1] -= dir_dict[d][1]
        else:
            route.append((vtx[0], vtx[1])) # 이동한 vertex 기록

    return route

def solution(dirs):
    dirs_list = list(dirs)
    road_set = set() # edge를 담는 set

    route = move(dirs_list)

    for i in range(len(route) - 1):
        st = route[i]
        end = route[i + 1]
        road_set.update([(st, end), (end, st)]) # 순서를 바꿔도 같은 길이므로 넣을 때 둘다 넣기

    return len(road_set) // 2 # 순서 바뀐것도 추가로 넣었으므로 개수가 2배로 나옴 그래서 나누기 2