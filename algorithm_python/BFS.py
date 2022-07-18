
def bfs(graph, start_node):
    queue = [start_node] # queue 이용
    visited = []

    while queue:
        node = queue.pop(0)

        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)

    return visited

# TODO : pop(0)는 O(N)??이라서 비효율적 deque 이용해서 해보기

# 예시 - graph는 딕셔너리 리스트 형태의 인접 리스트
if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    res = bfs(graph, "A")
    print(res)