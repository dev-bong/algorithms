import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []

    for oper in operations:
        op, num = oper.split(" ")
        num = int(num)

        if op == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        elif op == "D":
            if min_heap and max_heap: # 큐가 비어있을 때 삭제 연산은 무시
                if num == 1: # 최대값 삭제
                    max_val = heapq.heappop(max_heap)[1]
                    min_heap.remove(max_val)
                    heapq.heapify(min_heap)
                elif num == -1: # 최소값 삭제
                    min_val = heapq.heappop(min_heap)
                    max_heap.remove((-min_val, min_val))
                    heapq.heapify(max_heap)

    size = len(min_heap)
    if size > 0:
        return [max_heap[0][1], min_heap[0]]
    else:
        return [0, 0]

# TODO : heapify 안쓰고 푸는법??? heapify 시간복잡도는 얼마나 되는지?