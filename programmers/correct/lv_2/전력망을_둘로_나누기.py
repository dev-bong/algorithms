from copy import deepcopy
"""
dictionary에 대한 copy 메소드로 복사가 가능하지만 얕은 복사임
깊은 복사를 위해서는 copy 모듈의 deepcopy가 필요
"""

def dfs(graph, vertex):
    # dfs로 하나의 네트워크 추출
    stack = [vertex]
    visited = set()

    while stack:
        v = stack.pop()

        if v not in visited:
            visited.add(v)
            stack.extend(graph[v])
    return visited

def solution(n, wires):
    answer = n
    wire_conn = {i : [] for i in range(1, n+1)}
    towers = set([i for i in range(1, n+1)])
    
    for wire in wires:
        wire_conn[wire[0]].append(wire[1])
        wire_conn[wire[1]].append(wire[0])

    for wire in wires:
        wire_conn_dis1 = deepcopy(wire_conn)
        # edge 중에 하나 끊기
        wire_conn_dis1[wire[0]].remove(wire[1])
        wire_conn_dis1[wire[1]].remove(wire[0])

        # 네트워크 분리
        net1 = dfs(wire_conn_dis1, 1)
        remain = list(towers - net1) # 집합자료형은 인덱싱 지원 X
        net2 = dfs(wire_conn_dis1, remain[0])

        answer = min([abs(len(net1) - len(net2)), answer]) # 두 네트워크의 tower수 차이가 가장 적은 경우 고르기

    return answer