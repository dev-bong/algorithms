def solution(N, stages):
    fail_rate = []

    for i in range(1, N+1):
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