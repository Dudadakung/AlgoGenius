import sys

print = sys.stdout.write
input = sys.stdin.readline

N, M = map(int, input().split())

office = [[] for _ in range(N)]
coverd = [[False for _ in range(M)] for _ in range(N)]
cctvs = []
cctv_types = []
cctv_loc = []
cctv_cnt = 0

dir_cctv = [0, 1, 2, 3]
dir_cctv_2 = [0, 1]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        n = row[j]
        office[i].append(n)
        if n > 0 and n < 6:
            cctv_cnt += 1
            cctv_types.append(n)
            cctv_loc.append((i, j))
            if n == 2:
                cctvs.append(dir_cctv_2)
            elif n == 5:
                cctvs.append([5])
            else:
                cctvs.append(dir_cctv)


# dir - 방향
# 0 : 상
# 1 : 우
# 2 : 하
# 3 : 좌
def cover(r, c, dir):
    cnt = 0
    if dir == 0:
        cur = r
        while cur > 0:
            cur -= 1
            if office[cur][c] != 6 and not coverd[cur][c]:
                coverd[cur][c] = True
                cnt += 1
    elif dir == 1:
        cur = c
        while cur < M - 1:
            cur += 1
            if office[r][cur] != 6 and not coverd[r][cur]:
                coverd[cur][c] = True
                cnt += 1
    elif dir == 2:
        cur = r
        while cur < N - 1:
            cur += 1
            if office[cur][c] != 6 and not coverd[cur][c]:
                coverd[cur][c] = True
                cnt += 1
    elif dir == 3:
        cur = c
        while cur > 0:
            cur -= 1
            if office[r][cur] != 6 and not coverd[r][cur]:
                coverd[cur][c] = True
                cnt += 1


def cctv(r, c, type, dir):
    if type == 1:
        cctv_1(r, c, dir)
    if type == 2:
        cctv_2(r, c, dir)
    if type == 3:
        cctv_3(r, c, dir)
    if type == 4:
        cctv_4(r, c, dir)
    if type == 5:
        cctv_5(r, c)


def cctv_1(r, c, dir):
    cover(r, c, dir)


def cctv_2(r, c, dir):
    cover(r, c, dir)
    cover(r, c, dir + 2)


def cctv_3(r, c, dir):
    cover(r, c, dir)
    cover(r, c, (dir + 1) % 4)


def cctv_4(r, c, dir):
    cover(r, c, dir)
    cover(r, c, (dir + 1) % 4)
    cover(r, c, (dir + 2) % 4)


def cctv_5(r, c, dir):
    cover(r, c, 0)
    cover(r, c, 1)
    cover(r, c, 2)
    cover(r, c, 3)


print(str(cctvs))
print(str(cctv_loc))
print(str(cctv_types))


for dir in cctvs[0]:
    cctv(cctv_loc[0][0], cctv_loc[0][1], cctv_types[0], dir)
    for dir in cctvs[1]:
        cctv(cctv_loc[1][0], cctv_loc[1][1], cctv_types[1], dir)
        for dir in cctvs[2]:
            cctv(cctv_loc[2][0], cctv_loc[2][1], cctv_types[2], dir)
            for dir in cctvs[3]:
                cctv(cctv_loc[3][0], cctv_loc[3][1], cctv_types[3], dir)
                for dir in cctvs[4]:
                    cctv(cctv_loc[4][0], cctv_loc[4][1], cctv_types[4], dir)
                    for dir in cctvs[5]:
                        cctv(cctv_loc[5][0], cctv_loc[5][1], cctv_types[5], dir)
                        for dir in cctvs[6]:
                            cctv(cctv_loc[6][0], cctv_loc[6][1], cctv_types[6], dir)
                            for dir in cctvs[7]:
                                cctv(cctv_loc[7][0], cctv_loc[7][1], cctv_types[7], dir)
