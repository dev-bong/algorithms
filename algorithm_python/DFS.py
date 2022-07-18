
def dfs(graph, start_node):
    stack = [start_node] # stack 이용
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            stack.extend(graph[node])
            visited.append(node)
    
    return visited

# TODO : 재귀(recursion call) 이용해서 해보기

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

    res = dfs(graph, "A")
    print(res)