def solution(n, times):
    answer = -1
    times.sort()
    min_time, max_time = (0, times[-1] * n)

    while min_time < max_time:
        mid_time = (min_time + max_time) // 2
        process_people = sum([mid_time // time for time in times])

        if n <= process_people:
            max_time = mid_time # +1을 하지않고 높은쪽은 mid_time으로 고정
            answer = mid_time
        elif n > process_people:
            min_time = mid_time + 1

    return answer

"""
이진 탐색 lower bound, upper bound 참고!!
"""