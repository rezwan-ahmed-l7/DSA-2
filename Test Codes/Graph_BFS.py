from collections import deque

def BFS(G_adj, S, V_count):
    # Step 1-4: Initialize vertices (color = WHITE, d = inf, pi = NIL)
    color = {}
    d = {}
    pi = {}
    
    for u in range(1, V_count + 1):
        if u != S:
            color[u] = "white"
            d[u] = float('inf')
            pi[u] = None

    # Step 5-7: Initialize source vertex S
    color[S] = "gray"
    d[S] = 0
    pi[S] = None

    # Step 8-9: Initialize Queue Q and enqueue S
    Q = deque()
    Q.append(S)

    print("BFS Traversal Order:", end=" ")

    # Step 10: while Q != empty
    while len(Q) > 0:
        # Step 11: u = Dequeue(Q)
        u = Q.popleft()
        print(u, end=" ")

        # Step 12: for each v in G.adj[u]
        for v in G_adj[u]:
            # Step 13: if v.color == white
            if color[v] == "white":
                # Step 14-17:
                color[v] = "gray"
                d[v] = d[u] + 1
                pi[v] = u
                Q.append(v)
        
        # Step 18: u.color = black
    color[u] = "black"
    print()

G_adj = {
    1: [2, 5],
    2: [1, 5, 3, 4],
    3: [2, 4],
    4: [2, 3, 5],
    5: [1, 2, 4]
}

BFS(G_adj, S=1, V_count=5)