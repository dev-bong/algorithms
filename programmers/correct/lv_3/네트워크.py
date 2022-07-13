def bfs(n, graph, vertex):
    """
    bfs를 이용해 해당 vertex와 연결된 모든 vertex 탐색
    - 이렇게 연결된 vertex 집합이 곧 하나의 네트워크
    - 즉, vertex가 속한 네트워크를 리턴한다고 봐도 됨
    """
    queue = [vertex] # bfs는 queue를 이용. dfs는 stack으로 바꾸면 됨
    visited = [vertex]

    while queue:
        deq_item = queue.pop(0)

        for i in range(n):
            # 인접 행렬 값이 1(연결되어 있음)이고 방문한적 없는 노드 체크
            if graph[deq_item][i] == 1 and i not in visited:
                queue.append(i)
                visited.append(i)
    
    return visited
        

def solution(n, computers):
    answer = 0
    in_networks = set() # set으로 한 이유는 차집합 연산을 위해..
    remains = set([i for i in range(n)])

    while remains:
        pop_com = remains.pop() # 뒤에서 vertex 하나 뽑음

        # 해당 vertex가 속한 네트워크 추출해서 취합함
        in_networks.update(set(bfs(n, computers, pop_com)))
        remains = remains - in_networks # remains에서 추출한 네트워크 제거
        answer += 1

    return answer