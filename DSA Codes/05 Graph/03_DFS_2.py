from collections import defaultdict

def no_of_island(n, edges):
    adj_list = defaultdict(list)

    for i,j in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)

    visited = [False for _ in range(n + 1)]

    def dfs(s):
        if visited[s]:
            return

        visited [s] = True
        print(s, end = ' ')
        for i in adj_list[s]:
            dfs(i)

    cnt = 0
    for i in range(1, n+1):
        if visited[i] == False:
            dfs(i)
            cnt += 1

    print(cnt)

n = 5
edges = [(1,2), (1,4), (2,3), (2,5), (3,5), (4,5)]
no_of_island(n, edges)
