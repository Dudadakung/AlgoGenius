import sys

print = sys.stdout.write
input = sys.stdin.readline


def dfs(w, depth, cur):
    global cnt
    depth += 1

    cur += w
    cur -= K
    if cur < 0:
        return
    elif depth == N:
        cnt += 1
    else:
        for i in range(N):
            if not used[i]:
                used[i] = True
                dfs(weight[i], depth, cur)
                used[i] = False


N, K = map(int, input().split())

weight = list(map(int, input().split()))
used = [False for _ in range(N)]
cnt = 0


for i in range(N):
    used[i] = True
    dfs(weight[i], 0, 0)
    used[i] = False

print(str(cnt))
