# Global variable 'time'
time = 0

def DFS_VISIT(G_adj, u, color, d, f, pi):
    global time
    
    # Step 1-3: u newly discovered
    time = time + 1
    d[u] = time
    color[u] = "gray"

    # Step 4-7: Explore edge (u, v)
    for v in G_adj[u]:
        if color[v] == "white":
            pi[v] = u
            DFS_VISIT(G_adj, v, color, d, f, pi)

    # Step 8-10: Blacken u; it is finished
    color[u] = "black"
    time = time + 1
    f[u] = time


def DFS(G_adj, V_count):
    global time
    
    color = {}
    pi = {}
    d = {}
    f = {}

    # Step 1-3: For each vertex u in G.V
    for u in range(1, V_count + 1):
        color[u] = "white"
        pi[u] = None

    # Step 4: time = 0
    time = 0

    # Step 5-7: for each vertex u in G.V
    for u in range(1, V_count + 1):
        if color[u] == "white":
            DFS_VISIT(G_adj, u, color, d, f, pi)
            
    print("Vertex Discovery & Finish Times:")
    for u in range(1, V_count + 1):
        print(f"Vertex {u}: Discovery time (d) = {d[u]}, Finish time (f) = {f[u]}")

G_adj = {
    1: [2, 5],
    2: [5, 3, 4],
    3: [4],
    4: [],
    5: [4]
}

DFS(G_adj, V_count=5)