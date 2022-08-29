import math
import heapq

def dijkstra(graph, start):
    visited = set()
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


def solution(N, road, K):
    answer = 0
    graph = {i : {} for i in range(1, N + 1)}

    for rd in road:
        st, end, dis = rd
        ex_dis = 10001 # 문제에서 정의한 도로 최대 소요 시간
        if end in graph[st]:
            ex_dis = graph[st][end]
        graph[st][end] = min([dis, ex_dis])
        graph[end][st] = graph[st][end]

    min_dis = dijkstra(graph, 1)
    for node in min_dis:
        if min_dis[node] <= K:
            answer += 1

    return answer

"""
의외로 쉽게품;
다익스트라 알고리즘 보고 풀었으니까 쉽게푼건 아닌가?
"""