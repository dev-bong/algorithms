def room_check(room): # 해당 방에 있는 모두가 거리두기를 지켰는지 체크
    room_dict = {
        "P" : [],
        "X" : [],
        "O" : []
    }

    for i in range(5):
        for j in range(5):
            room_dict[room[i][j]].append((i, j)) # 각 칸이 P, X, O 중에 무엇인지에 따라 딕셔너리에 넣기

    for i in range(len(room_dict["P"])):
        for j in range(len(room_dict["P"])):
            if i == j:
                continue
            a, b = room_dict["P"][i]
            c, d = room_dict["P"][j]

            dist = abs(a - c) + abs(b - d) # 사람 간의 거리 계산 (맨해튼 거리)
            if dist == 1: # 거리가 1인 경우는 무조건 안지킨 것
                return 0
            elif dist == 2: # 거리 2인 경우
                if a == c: # 직선 상에 있는 경우 1
                    if (a, (b + d)//2) in room_dict["O"]:
                        return 0
                elif b == d: # 직선 상에 있는 경우 2
                    if ((a + c)//2, b) in room_dict["O"]:
                        return 0
                else: # 대각선에 있는 경우
                    if (a, d) in room_dict["O"] or (c, b) in room_dict["O"]:
                        return 0
            # 거리가 3 이상이면 거리두기 지킨 것
    return 1


def solution(places):
    answer = []
    for room in places:
        answer.append(room_check(room))
    return answer