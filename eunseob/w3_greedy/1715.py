from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline())

nums = []

for _ in range(N):
    heappush(nums, int(sys.stdin.readline()))

total = 0
for i in range(1, N):
    m1 = heappop(nums)
    m2 = heappop(nums)
    cur = m1 + m2
    total += cur
    heappush(nums, cur)

print(total)


"""
10 20 25 28
1.
30 25 40 - 30
55 28 - 85
83 - 168
2.
30 25 28 - 30
53 30 - 83
83 - 166
"""
