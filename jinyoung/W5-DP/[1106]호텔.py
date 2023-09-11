from sys import stdin

def solve():
    for cost in range(1, 100001):
        for t in town:
            if cost - t[0] >= 0:
                dp[cost] = max(dp[cost - t[0]] + t[1], dp[cost])

        if dp[cost] >= C:
            return cost
        
C, N = map(int, stdin.readline().split())
town = []
dp = [0 for _ in range(100001)]

for _ in range(N):
    town.append(list(map(int, stdin.readline().split())))

print(solve())
