import sys
from collections import deque

N = int(input())
deque = []; d = 0
for i in range (N):
    deque.append(int(sys.stdin.readline()))
deque.sort()
for i in range (N):
    d += abs(i - deque[i] + 1)
print(d)