
#! 첫번째 풀이.. 효율성 테스트 모두 실패
def solution(stones, k):
    if len(stones) == 1:
        return stones[0]
    max_stone = max(stones)
    for answer in range(1, max_stone + 1):
        jump = 0
        for i in range(len(stones)):
            if stones[i] < answer:
                jump += 1
            else:
                jump = 0
            
            if jump >= k:
                return answer - 1

# TODO : 이진탐색 이용??? 탐색 범위를 이진탐색을 이용해서 줄이기?


#! 슬라이딩 윈도우? 기법 이용해봄 (효율성 13번만 실패)
from collections import deque

def solution(stones, k):
    if len(stones) == 1: #? 징검다리 한칸인 경우
        return stones[0]
    if k == 1: #? k = 1 일때는 징검다리 중 하나만 0이되어도 못건넘
        return min(stones)
    answer = []
    window = deque([])

    window.extend(stones[:k])
    window_max = max(window)
    answer.append(window_max)

    for i in range(k, len(stones)):
        w_out = window.popleft()
        if w_out == window_max: # out 값이 최대값이랑 같은 경우
            window_max = max(window)
        w_in = stones[i]
        window.append(w_in)
        if w_in > window_max:
            window_max = w_in
        answer.append(window_max)

    return min(answer)


#! 슬라이딩 윈도우 - 인덱스를 윈도우에.. (풀이 완료)
# TODO : 이해 필요 (https://leetcode.com/problems/sliding-window-maximum/solutions/237611/Simplest-O(n)-Python-Solution-with-Explanation/)
from collections import deque

def solution(stones, k):
    if len(stones) == 1:
        return stones[0]
    if k == 1:
        return min(stones)
    window = deque([])
    answer = []

    for i, stone in enumerate(stones):
        while window and stones[window[-1]] < stone:
            window.pop()
        window.append(i)

        if window[0] == i - k:
            window.popleft()
        if i >= (k - 1):
            answer.append(stones[window[0]])

    return min(answer)