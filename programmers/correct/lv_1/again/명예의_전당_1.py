import heapq

def solution(k, score):
    answer = []
    min_heap = [] # top k 저장

    for day in range(len(score)):
        if len(min_heap) < k:
            heapq.heappush(min_heap, score[day])
            answer.append(min_heap[0]) # min_heap[0] 는 heap tree의 root node
        else:
            if min_heap[0] < score[day]: # top k 안에 드는 점수면..
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, score[day])
            answer.append(min_heap[0])
    return answer