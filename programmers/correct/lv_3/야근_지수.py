import heapq

def solution(n, works):
    if sum(works) <= n: # 퇴근까지 남은 n시간 내에 남은일을 다 할 수 있을 때
        return 0
    
    works_heap = []
    for w in works: #* 정렬하지 않고 최대값을 구하기 위해 heap을 이용
        heapq.heappush(works_heap, (-w, w))

    while n:
        _, max_w = heapq.heappop(works_heap) # 현재 최대값 pop
        heapq.heappush(works_heap, (- (max_w - 1), max_w - 1)) # 1뺀뒤 다시 넣기
        n -= 1

    answer = 0
    for wh in works_heap:
        answer += wh[1] ** 2
    return answer

"""
각 요소의 제곱의 합이 최소가 되려면??
    >> 현재 works의 최대값을 1씩 빼주면서 총 n을 빼주면 됨
"""

#! 아래는 효율성 테스트 탈락 풀이
def solution(n, works):
    if sum(works) <= n: # 퇴근까지 남은 n시간 내에 남은일을 다 할 수 있을 때
        return 0
    
    while n:
        works.sort() #! 현재 works의 최대값을 구하기 위해 매 회차 정렬하는 것이 시간이 너무 오래걸림
        works[-1] -= 1
        n -= 1
    
    answer = 0
    for w in works:
        answer += w ** 2
    return answer