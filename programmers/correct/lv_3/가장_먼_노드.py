def solution(n, edge):
    graph = {i : [] for i in range(1, n+1)} # (노드 : 해당 노드와 연결된 노드들 리스트)
    distance_from_1 = {} # (노드 1로부터 거리 : 해당 거리인 노드들 리스트)
    peek = set([1]) # 방문할 노드
    visited = set([1]) # 방문한 노드

    for e in edge: # graph 딕셔너리 만들기
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    distance = 0
    while len(visited) < n: # 노드1로부터의 거리가 0, 1, 2, ... 인 순으로 탐방. BFS 형식?
        distance_from_1[distance] = []
        for p in peek:
            if p not in visited:
                distance_from_1[distance].append(p)
                visited.add(p)
        
        tmp = set()
        for p in peek: # 거리 n인 노드들에 연결된 노드들을 수집
            tmp = tmp | set(graph[p])
        peek = tmp - visited # 방문했던 노드는 제외
        distance += 1
    
    max_distance = max(distance_from_1.keys())

    return len(distance_from_1[max_distance])

# TODO : BFS? (지금 한게 BFS인거 같긴한데), 다익스트라?, 벨만포드?