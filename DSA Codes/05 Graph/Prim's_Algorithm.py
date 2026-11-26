import heapq

def prims_algorithm(graph):

    visited = [False] * len(graph)
    visited[0] = True

    pq = []
    for dest, weight in graph[0]:
        heapq.heappush(pq, (weight, 0, dest))

    mst = []
    total = 0

    while pq:
        weight, src, dest = heapq.heappop(pq)

        if visited[dest]:
            continue

        print(chr(src + 65), "->", chr(dest + 65), "weight:", weight)

        visited[dest] = True
        mst.append((src, dest, weight))
        total += weight

        for neighbor, w in graph[dest]:
            if not visited[neighbor]:
                heapq.heappush(pq, (w, dest, neighbor))

    return total, mst


graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

total, mst = prims_algorithm(graph)
print("MST total weight:", total)
print("MST edges (src, dest, weight):", mst)