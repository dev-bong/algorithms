import math
import heapq

def dijkstra(graph, start): # dijkstra 알고리즘 (start부터 각 지점까지 최단거리 구하기)
    nodes = graph.keys()
    min_heap = [] # (현재까지 계산된 거리, 노드)
    distance = {}

    for n in nodes:
        if n == start:
            heapq.heappush(min_heap, (0, n))
            distance[n] = 0
            continue
        heapq.heappush(min_heap, (math.inf, n)) # 무한대값
        distance[n] = math.inf

    while min_heap:
        d, cur = heapq.heappop(min_heap)

        linked = graph[cur].keys()
        for nxt in linked:
            dis = graph[cur][nxt]
            if distance[nxt] > (distance[cur] + dis):
                min_heap.remove((distance[nxt], nxt))

                distance[nxt] = distance[cur] + dis
                heapq.heappush(min_heap, (distance[nxt], nxt))
                heapq.heapify(min_heap)

    return distance

def solution(n, s, a, b, fares):
    answer = []
    graph = {i : {} for i in range(1, n + 1)}

    for fare in fares: # graph 만들기
        st, end, cost = fare

        graph[st][end] = cost
        graph[end][st] = cost

    a_dis = dijkstra(graph, a) # a부터 각지점까지 최단거리
    b_dis = dijkstra(graph, b) # b부터 각지점까지 최단거리
    start_dis = dijkstra(graph, s) # s부터 각지점까지 최단거리
    
    # s부터 share_point까지는 합승하고 그 후부터 따로 타고다는 경우 계산 (share_point에 s도 포함)
    for share_point in start_dis.keys():
        tmp = start_dis[share_point] # share_point 까지 합승
        tmp += a_dis[share_point] # 그 이후 따로 타고 가기
        tmp += b_dis[share_point]
        answer.append(tmp)

    return min(answer)