import sys

print = sys.stdout.write
input = sys.stdin.readline
sys.setrecursionlimit(100000000)


N, M, R = map(int, input().split())
visited = [False for _ in range(N + 1)]
graph = [list() for _ in range(N + 1)]
depth = [-1 for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()


def dfs(d, R):
    visited[R] = True
    depth[R] = d
    for x in graph[R]:
        if not visited[x]:
            dfs(d + 1, x)


dfs(0, R)

for result in range(1, N + 1):
    print(str(depth[result]) + "\n")
