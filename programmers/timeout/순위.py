def get_players(res, player, direction, win_lose):
    # 해당 플레이어보다 상위 또는 하위에 있는 모든 플레이어 수집. direction에 따라 상위, 하위 바뀜
    vertex = set()

    candidate = res[player][direction]
    while True:
        if candidate:
            vertex.update(candidate)
            tmp = []
            for c in candidate:
                if c in win_lose: # 이미 계산했던 것이면 결과만 합치고 패스
                    vertex.update(win_lose[c][direction])
                else:
                    tmp += res[c][direction]
            candidate = tmp
        else:
            break

    return vertex


def solution(n, results):
    answer = 0
    result_dict = {i : {"win" : set(), "lose" : set()} for i in range(1, n+1)} # 입력을 토대로 해당 플레이어에게 이긴, 진 플레이어 정보 저장
    win_lose = {}

    for r in results:
        result_dict[r[0]]["win"].add(r[1])
        result_dict[r[1]]["lose"].add(r[0])

    for i in range(1, n+1):
        up = get_players(result_dict, i, "lose", win_lose)
        down = get_players(result_dict, i, "win", win_lose)
        win_lose[i] = {"win" : down, "lose" : up} # 시간을 줄이기 위해 이미 계산한 것들은 저장
        if (n - 1) == len(up | down):
            answer += 1

    return answer

"""
1. BFS, DFS 이런거 잘 모르고 그냥 풀어봤는데 테스트 5 부터 시간초과
2. 이미 계산한 것들은 저장해서 시간을 줄이려고 했으나 테스트 7 부터 시간초과
    - 시간이 줄어들긴 함
"""