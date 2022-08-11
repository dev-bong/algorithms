
##### ! 초기버전
def solution(n, times):
    answer = -1
    times.sort() # max_time을 구하기 위해 정렬
    min_time, max_time = (0, times[-1] * n)

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        process_people = sum([mid_time // time for time in times]) # mid_time에 사람을 총 몇명 처리할수 있는지 계산

        if min_time == max_time: # while문 다 돌때까지 answer를 못찾는 경우가 있어서 추가
            if process_people >= n:
                answer = mid_time # answer 못찾으면 그때의 mid_time으로

        if n < process_people:
            max_time = mid_time - 1
        elif n > process_people:
            min_time = mid_time + 1
        else:
            answer = mid_time
            break

    # 같은 process_people 값을 가지는 mid_time이 여러개 있을 수 있음
    # answer를 -1씩 해가면서 같은 process_people을 갖는 최소 time을 찾는 것
    # 여기서 시간이 많이걸림
    while True:
        process_people = sum([(answer - 1) // time for time in times])
        if n == process_people:
            answer -= 1
        else:
            break

    return answer
"""
문제
1. 시간초과
2. answer이 부정확하거나 찾아내지 못하는 경우 있음
    - 2, [1, 2, 2, 2, 100] res = 2 테케 6에 가까운듯?
    - 10, [6,8,10] res = 30
"""


##### ! 수정버전
def solution(n, times):
    answer_list = [] # answer 후보 리스트 생성
    answer = -1
    times.sort()
    min_time, max_time = (0, times[-1] * n)

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        process_people = sum([mid_time // time for time in times])

        if n < process_people:
            max_time = mid_time - 1
            answer_list.append(mid_time) # 처리인원이 n보다 많은 경우도 정답 가능하므로 정답 후보 리스트에 넣기
        elif n > process_people:
            min_time = mid_time + 1
        else:
            answer_list.append(mid_time)
            break

    answer = min(answer_list) # 뽑힌 정답 후보중에 최소값 추출

    # 정답 최소값과 같은 process_people을 가지는 최소값 또다시 추출
    while True:
        process_people = sum([(answer - 1) // time for time in times])
        if n == process_people:
            answer -= 1
        else:
            break

    return answer
"""
문제
1. 시간초과 (정답은 다 맞는듯)
    - 케이스 7,8 시간초과
"""