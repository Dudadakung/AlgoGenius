# 2023/09/12 
from sys import stdin
import sys

sys.setrecursionlimit(2*10**5)

def dfs(node, depth):
    depth_list[node] = depth
    for n in line[node]:    
        if not visited[n]:
            visited[n] = True
            dfs(n, depth + 1)

N, M, R = map(int, stdin.readline().split())

line = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
depth_list = [-1 for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    line[u].append(v)
    line[v].append(u)

for i in range(1, N + 1):
    line[i].sort()

visited[R] = True

dfs(R, 0)

for i in range(1, N + 1):
    print(depth_list[i])