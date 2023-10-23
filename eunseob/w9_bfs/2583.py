import sys
from collections import deque

print = sys.stdout.write
input = sys.stdin.readline

N, M, K = map(int, input().split())

grid = [[False for _ in range(M)] for _ in range(N)]

for _ in range(K):
    m1, n1, m2, n2 = map(int, input().split())
    for n in range(n1, n2):
        for m in range(m1, m2):
            grid[n][m] = True

size = []


def bfs(n, m):
    q = deque()
    q.append([n, m])
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1

        if x + 1 < N:
            if not grid[x + 1][y]:
                grid[x + 1][y] = True
                q.append([x + 1, y])
        if x - 1 > -1:
            if not grid[x - 1][y]:
                grid[x - 1][y] = True
                q.append([x - 1, y])
        if y + 1 < M:
            if not grid[x][y + 1]:
                grid[x][y + 1] = True
                q.append([x, y + 1])
        if y - 1 > -1:
            if not grid[x][y - 1]:
                grid[x][y - 1] = True
                q.append([x, y - 1])

    return cnt


for n in range(N):
    for m in range(M):
        if not grid[n][m]:
            grid[n][m] = True
            size.append(bfs(n, m))


size.sort()

print(str(len(size)) + "\n")
for result in size:
    print(str(result) + " ")
