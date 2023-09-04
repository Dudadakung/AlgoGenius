import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
s = deque()

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push":
        s.append(int(cmd[1]))

    if cmd[0] == "pop":
        if not s:
            print(-1)
        else:
            print(s.pop())

    if cmd[0] == "size":
        print(len(s))

    if cmd[0] == "empty":
        if not s:
            print(1)
        else:
            print(0)

    if cmd[0] == "top":
        if not s:
            print(-1)
        else:
            print(s[-1])
