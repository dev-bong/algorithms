from collections import deque
# popleft로 시간 복잡도 줄이기 위해 이용

def move(q1, q2): # q1 -> q2로 원소 이동
    item = q1.popleft()
    q2.append(item)
    return item # 이동시킨 item 리턴

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    size = len(queue1 + queue2)

    while True:
        # sum이 큰 쪽 queue에서 작은 쪽 queue로 이동
        if q1_sum > q2_sum:
            item = move(queue1, queue2)
            q1_sum -= item
            q2_sum += item
        elif q1_sum < q2_sum:
            item = move(queue2, queue1)
            q1_sum += item
            q2_sum -= item
        else:
            break
        
        if answer > (size * 2):
            # 무슨 방법을 써도 되지 않는 경우 -1 리턴
            #! (size * 2)는 대강 이렇겠지 해서 정한 값.. 명확한 기준은 없음
            return -1

        answer += 1

    return answer

"""
# TODO : -1 리턴하는 경우 최고로 많은 경우는??
1. queue 하나의 최대 길이는 300000 이므로 answer =  600000 까지 해보기?
2. 방법이 없는 경우 특정 패턴을 반복하게 된다.. 이것의 최대 길이는?
"""