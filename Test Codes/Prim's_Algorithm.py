import heapq

def prims_algorithm(graph, start_node):
    mst_edges = []
    visited = set([start_node])
    
    # Priority Queue: (weight, u, v)
    edges = [
        (weight, start_node, to_node) 
        for to_node, weight in graph[start_node]
    ]
    heapq.heapify(edges)
    
    total_cost = 0

    while edges:
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, weight))
            total_cost += weight
            
            for next_node, next_weight in graph[v]:
                if next_node not in visited:
                    heapq.heappush(edges, (next_weight, v, next_node))

    print("MST Edges (u, v, weight):", mst_edges)
    print("Total Cost:", total_cost)

# Graph representation: adj list with (neighbor, weight)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

prims_algorithm(graph, start_node=0)