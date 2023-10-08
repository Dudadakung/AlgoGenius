import sys

print = sys.stdout.write
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    i1, i2 = map(int, input().split())
    graph[i1].append(i2)
    graph[i2].append(i1)


def dfs(v, d):
    if d == 5:
        print("1")
        exit(0)
    else:
        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = True
                dfs(adj, d + 1)
                visited[adj] = False


for v in range(N):
    visited[v] = True
    dfs(v, 1)
    visited[v] = False

print("0")
