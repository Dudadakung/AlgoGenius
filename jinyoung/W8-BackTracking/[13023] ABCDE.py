# 2023/09/26
from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(5000000)

global ans

def dfs(n, depth):
    global ans
    is_used[n] = True
    if depth >= 4:
        ans = 1
        return
    else:
        for i in people[n]:
            if not is_used[i]:
                dfs(i, depth + 1)
                is_used[i] = False

N, M = map(int, stdin.readline().split())
people = [[] for _ in range(N)]
ans = 0

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    people[a].append(b)
    people[b].append(a)

for i in range(N):
    is_used = [False for _ in range(N)]
    dfs(i, 0)

print(ans)
