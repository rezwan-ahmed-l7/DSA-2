from collections import defaultdict
from collections import deque

def bfs(n, edges):
    adj = defaultdict(list)

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    q = deque()
    start = 1

    q.append(start)
    visited = [False for _ in range(n + 1)]
    visited[1] = True

    while q:
        s = q.popleft()
        print(s, end = ' ')

        for u in adj[s]:
            if visited[u]:
                continue

            visited[u] = True
            q.append(u)

n = 5
edges = [(1,2), (1,4), (2,3), (2,5), (3,5), (4,5)]
bfs(n, edges)
