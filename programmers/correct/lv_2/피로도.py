from itertools import permutations

def solution(k, dungeons):
    """
    k : 현재 피로도
    dungeongs : 던전 별 (요구 피로도, 소모 피로도)의 리스트 (던전은 최대 8개)
    """
    answer = 0
    dungeon_nums = len(dungeons)
    dungeon_idx = [i for i in range(dungeon_nums)]
    clear_routes = permutations(dungeon_idx, dungeon_nums) # 던전들을 방문하는 순서에 대한 모든 경우의 수

    for c_route in clear_routes:
        now_fatigue = k
        clear_dungeons = 0

        for d_idx in c_route: # 각 경우 마다 던전을 몇개까지 방문할 수 있는지 계산
            need, consume = dungeons[d_idx]
            if now_fatigue >= need:
                now_fatigue -= consume
                clear_dungeons += 1
            else:
                break
        
        answer = max((clear_dungeons, answer)) # 던전 최대 클리어 수 저장
        
    return answer