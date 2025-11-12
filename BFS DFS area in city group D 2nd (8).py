# DFS using adjacency matrix
def dfs(graph, start, visited):
    print(start, end=" ")
    visited[start] = True
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

# BFS using adjacency list
from collections import deque
def bfs(graph, start):
    visited = set()
    q = deque([start])
    while q:
        v = q.popleft()
        if v not in visited:
            print(v, end=" ")
            visited.add(v)
            q.extend(graph[v])

# -------- MAIN PROGRAM --------
# Locations: A, B, C, D
# Graph connections: A-B, A-C, B-D, C-D
adj_matrix = [
    [0,1,1,0],  # A
    [1,0,0,1],  # B
    [1,0,0,1],  # C
    [0,1,1,0]   # D
]

print("DFS (Adjacency Matrix) from A:")
dfs(adj_matrix, 0, [False]*4)

adj_list = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A','D'],
    'D': ['B','C']
}

print("\nBFS (Adjacency List) from A:")
bfs(adj_list, 'A')