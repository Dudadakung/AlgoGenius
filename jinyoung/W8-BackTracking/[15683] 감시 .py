# 2023/09/27
from sys import stdin
from copy import deepcopy

global ans
global can_see

def cctv_type(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 2]
    if n == 3:
        return [0 , 1]
    if n == 4:
        return [0, 1, 3]
    if n == 5:
        return [0, 1, 2 ,3]

def see_up(x,y,t):
    while y >= 0:
        if room[y][x] == 6:
            break
        can_see[y][x] = t
        y -= 1
def see_right(x,y,t):
    while x < M:
        if room[y][x] == 6:
            break
        can_see[y][x] = t
        x += 1

def see_down(x,y,t):
    while y < N:
        if room[y][x] == 6:
            break
        can_see[y][x] = t
        y += 1

def see_left(x,y,t):
    while x >= 0:
        if room[y][x] == 6:
            break
        can_see[y][x] = t
        x -= 1

def count_cant_see():
    global ans
    cur_ans = 0
    for i in range(N):
        for j in range(M):
            if not can_see[i][j] and room[i][j] != 6:
                cur_ans += 1
    ans = min(ans, cur_ans)


def dfs(num):
    global can_see
    if num == len(cctv):
        count_cant_see()
        return
    y = int(cctv[num] / M)
    x = cctv[num] % M

    before_see = deepcopy(can_see)

    for i in range(4):
        cctv_view = cctv_type(room[y][x])
        for j in cctv_view:
            j = (j + i) % 4
            if j == 0:
                see_up(x, y,True)
            if j == 1:
                see_right(x,y,True)
            if j == 2:
                see_down(x,y,True)
            if j == 3:
                see_left(x,y,True)
        dfs(num + 1)
        can_see = deepcopy(before_see)

N, M = map(int, stdin.readline().split())
room = []
cctv = []
can_see = [[False for _ in range(M)] for i in range(N)]
ans = 65

for i in range(N):
    line = list(map(int, stdin.readline().split()))
    room.append(line)
    for j in range(M):
        if line[j] > 0 and line[j] <= 5:
            cctv.append(i*M + j)

see_degree = [[False for _ in range(4)] for i in range(len(cctv))]

dfs(0)

print(ans)