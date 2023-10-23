from sys import stdin
from collections import deque

n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
m = int(stdin.readline())
connect = [[] for _ in range(n + 1)]
is_in = [False for _ in range(n + 1)]
ans = -1

while m > 0:
    q, w = map(int, stdin.readline().split())
    connect[q].append(w)
    connect[w].append(q)
    m -= 1

que = deque()

que.append((a,0))

while que:
    node, weight = que.popleft()
    if node == b:
        ans = weight
        break
    for neighbor in connect[node]:
        if not is_in[neighbor]:
            is_in[neighbor] = True
            que.append((neighbor, weight + 1))

print(ans)