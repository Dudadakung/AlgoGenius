import sys

input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(100000000)

N, M = map(int, input().split())
visited = [False for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


def dfs(N):
    visited[N] = True
    for x in graph[N]:
        if not visited[x]:
            dfs(x)


count = 0
for n in range(1, N + 1):
    if not visited[n]:
        dfs(n)
        count += 1

print(str(count))
