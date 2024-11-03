from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

remain_before = [0 for _ in range(N + 1)]
after = [[] for _ in range(N + 1)]
complete_subject = [1 for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, stdin.readline().split())
    remain_before[b] += 1
    after[a].append(b)

que = deque()

for i in range(1, N+1):
    if remain_before[i] == 0:
        que.append((i, 1))

while que:
    num, cnt = que.popleft()
    complete_subject[num] = cnt
    for af_num in after[num]:
        remain_before[af_num] -= 1
        if remain_before[af_num] == 0:
            que.append((af_num, cnt + 1))
del complete_subject[0]
print(*complete_subject)