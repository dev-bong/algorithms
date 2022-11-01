def solution(distance, scope, times):
    # scope, time 모두 i번째 경비병에 대한 정보를 가지고 있으므로 같이 정렬하기 위해 합쳐줌
    scope_time = [sorted(scope[i]) + times[i] for i in range(len(scope))]
    #! scope의 경우 [11, 10] 같은 앞이 더 큰 경우가 올 수 있기 때문에 정렬해서 넣어줘야함
    scope_time.sort(key = lambda r: r[0])

    for st in scope_time:
        front, end, work_time, rest_time = st

        for t in range(front, end + 1):
            if t % (work_time + rest_time) > 0 and t % (work_time + rest_time) <= work_time:
                return t

    return distance