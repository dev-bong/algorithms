def solution(N, stages):
    fail_rate = []

    for i in range(1, N+1): #! 이중 for문이라서 시간복잡도 O(n^2)
        challenge = 0
        success = 0
        for stage in stages:
            if stage >= i:
                challenge += 1
            if stage > i:
                success += 1
        if challenge == 0: # 스테이지에 도달한 유저가 없는 경우
            fail_rate.append([0, i])
        else:
            fail_rate.append([1 - success/challenge, i])
    fail_rate.sort(key=lambda r: (r[0], -r[1]), reverse=True) # 기준 2개로 정렬. 앞에가 우선 기준. "-" 붙이면 설정된 순서의 반대로
    print(fail_rate)
    return [fr[1] for fr in fail_rate]

##### * 시간복잡도 줄인 풀이 #####
def solution(N, stages):
    fail_rate = []
    stage_at_users = {}

    for stage in stages: # stage 당 유저 수 딕셔너리로 저장
        if stage in stage_at_users:
            stage_at_users[stage] += 1
        else:
            stage_at_users[stage] = 1
    
    challengers = len(stages)
    for i in range(1, N+1): # 각 stage에서 실패한 유저들로 실패율 계산
        if i in stage_at_users:
            fail_users = stage_at_users[i]
            if challengers:
                fail_rate.append([fail_users/challengers, i])
            else:
                fail_rate.append([0, i])
            challengers -= fail_users
        else:
            fail_rate.append([0, i])
    
    fail_rate.sort(key=lambda r: (r[0], -r[1]), reverse=True)
    return [fr[1] for fr in fail_rate]