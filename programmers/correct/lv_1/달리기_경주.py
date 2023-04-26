
#! 시간초과
def swap(idx1, idx2 , li):
    tmp = li[idx1]
    li[idx1] = li[idx2]
    li[idx2] = tmp

def solution(players, callings):
    for call in callings:
        idx = players.index(call)
        swap(idx, idx-1, players)
    return players


#* 통과
"""
r_p : key=순위, value=플레이어 이름
p_r : key=플레이어 이름, value=순위

p_r 로 앞 플레이어를 전체탐색 없이 찾고
r_p 로 순위에 따른 플레이어 나열 조회 가능
"""
def swap(idx1, idx2 , li):
    tmp = li[idx1]
    li[idx1] = li[idx2]
    li[idx2] = tmp

def solution(players, callings):
    answer = []
    r_p = dict()
    p_r = dict()

    for i in range(len(players)):
        r_p[i] = players[i]
        p_r[players[i]] = i
    
    for call in callings:
        cur_rank = p_r[call]
        front_player = r_p[cur_rank - 1]
        swap(cur_rank, cur_rank-1, r_p)
        swap(front_player, call, p_r)

    
    for i in range(len(players)):
        answer.append(r_p[i])
    return answer