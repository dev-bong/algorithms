import heapq

def solution(n, k, enemy):
    round = 0
    rounds = len(enemy)
    ex_rounds = []
    
    if k >= rounds:
        return rounds

    while round < rounds:
        heapq.heappush(ex_rounds, (-enemy[round], enemy[round]))
        n -= enemy[round]

        if n < 0: # 이번 라운드 못버팀
            if k: # 무적권 남아있음
                while True:
                    k -= 1
                    overpower = heapq.heappop(ex_rounds)[1]
                    n += overpower
                    #? 무적권 한번 썼는데 그래도 -일 경우
                    if n >= 0:
                        break
                    else:
                        if k == 0:
                            return round
                    #? 물음표 부분 코드는 없어도 통과 되긴함..
            else: # 무적권 없음
                break
        round += 1
    
    return round


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))