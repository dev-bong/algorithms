import heapq

def solution(n, times):
    cost_heap = [(times[i], i) for i in range(len(times))]
    heapq.heapify(cost_heap)

    while n > 1:
        idx_cost, idx = heapq.heappop(cost_heap)
        heapq.heappush(cost_heap, (idx_cost + times[idx], idx))

        n -= 1

    return cost_heap[0][0]

"""
원래 이진탐색 문제지만 아직 이진탐색에 익숙치않아 heap을 이용해서 풀어봄
테스트 6,7,8,9 시간초과 발생
"""