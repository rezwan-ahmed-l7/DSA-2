class DSU:
    # Disjoint Set Union (DSU) helper structure
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def kruskal(vertices, edges):
    # Step 1: Sort all edges in non-decreasing order of their weight
    edges.sort(key=lambda item: item[2])
    
    dsu = DSU(vertices)
    mst = []
    total_cost = 0

    # Step 2: Pick the smallest edge and check if it forms a cycle
    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    print("Edges in MST (u, v, weight):", mst)
    print("Total Minimum Cost:", total_cost)

# Graph representation: (u, v, weight)
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
vertices = 4

kruskal(vertices, edges)