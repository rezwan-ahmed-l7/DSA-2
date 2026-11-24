import heapq

def dijkstra(adj, src):
    N = len(adj)

    pq = []
    dist = [float('inf')] * N

    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue
        for x in adj[u]:
            v = x[0]
            weight = x[1]

            if d + weight < dist[v]:
                dist[v] = d + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


adj = [
    [[1, 1], [2, 4]],
    [[0, 1], [2, 2], [3, 5]],
    [[0, 4], [1, 2], [3, 1]],
    [[1, 5], [2, 1]],
]

src = 0
dist = dijkstra(adj, src)
print(dist)