# 2023/09/16
from sys import stdin
from collections import deque

global cnt

def dfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.pop()
        for ny, nx in (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1):
            if board[ny][nx] > 0 and not is_in[ny][nx]:
                is_in[ny][nx]= True
                cnt += 1
                q.append((nx, ny))
    

N, M = map(int, stdin.readline().split())
board = []
ans = 0

for _ in range(N):
    board.append(list(map(int, stdin.readline().split())))

while True:
    remain_que = []
    que = deque()
    is_in = [[False for _ in range(M)] for i in range(N)]
    ans += 1

    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] > 0:
                reduce = 0
                for ny, nx in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if board[ny][nx] <= 0:
                        reduce += 1
                que.append((i,j, reduce))
                if board[i][j] - reduce > 0:
                    remain_que.append([j, i])
    while que:
        y,x,reduce = que.pop()
        board[y][x] -= reduce

    if not remain_que:
        ans = 0
        break
    
    is_in[remain_que[0][1]][remain_que[0][0]] = True
    cnt = 1
    dfs(remain_que[0][0], remain_que[0][1])
    if len(remain_que) != cnt:
        break
    
print(ans)


