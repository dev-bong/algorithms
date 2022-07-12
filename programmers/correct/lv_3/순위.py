def bfs(graph, start):
    queue = [start]
    visited = [start]

    while queue:
        vertex = queue.pop(0)

        for v in graph[vertex]:
            if v not in visited:
                queue.append(v)
                visited.append(v)
    return visited


def solution(n, results):
    answer = 0
    win_graph = {i : [] for i in range(1, n+1)}
    lose_graph = {i : [] for i in range(1, n+1)}

    for r in results:
        win_graph[r[0]].append(r[1])
        lose_graph[r[1]].append(r[0])

    for i in range(1, n+1):
        wins = bfs(win_graph, i)
        loses = bfs(lose_graph, i)
        print(i, wins, loses)
        if (n + 1) == (len(wins) + len(loses)):
            answer += 1

    return answer