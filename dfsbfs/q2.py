# BFS

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
graph = [
    [],             # node 0
    [2, 3, 8],      # node 1
    [1, 7],         # node 2
    [1, 4, 5],      # node 3
    [3, 5],         # node 4
    [3, 4],         # node 5
    [7],            # node 6
    [2, 6, 8],      # node 7
    [1, 7]          # node 8
]

visited = [False] * 9
bfs(graph, 1, visited)