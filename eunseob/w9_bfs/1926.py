import sys
from collections import deque

print = sys.stdout.write
input = sys.stdin.readline

N, M = map(int, input().split())

grid = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]


def bfs(x, y):
    q.append((x, y))
    size = 0

    while q:
        x, y = q.popleft()
        size += 1

        if x + 1 < N and not visited[x + 1][y] and grid[x + 1][y] == 1:
            visited[x + 1][y] = True
            q.append((x + 1, y))
        if x - 1 > -1 and not visited[x - 1][y] and grid[x - 1][y] == 1:
            visited[x - 1][y] = True
            q.append((x - 1, y))
        if y + 1 < M and not visited[x][y + 1] and grid[x][y + 1] == 1:
            visited[x][y + 1] = True
            q.append((x, y + 1))
        if y - 1 > -1 and not visited[x][y - 1] and grid[x][y - 1] == 1:
            visited[x][y - 1] = True
            q.append((x, y - 1))

    return size


for n in range(N):
    row = list(map(int, input().split()))
    for m in range(M):
        grid[n][m] = row[m]

q = deque()
size_list = []

for i in range(N):
    for j in range(M):
        if not visited[i][j] and grid[i][j] == 1:
            visited[i][j] = True
            size_list.append(bfs(i, j))

if size_list:
    print(str(len(size_list)) + "\n" + str(max(size_list)))
else:
    print("0" + "\n" + "0")
