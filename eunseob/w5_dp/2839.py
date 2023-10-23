N = int(input())

dp = [-1 for _ in range(5001)]
dp[3] = 1
dp[5] = 1
dp[6] = 2
dp[8] = 2

for i in range(6, N + 1):
    if dp[i - 3] + dp[i - 5] == -2:
        dp[i] = -1
    else:
        if dp[i - 3] == -1:
            dp[i] = dp[i - 5] + 1
        elif dp[i - 5] == -1:
            dp[i] = dp[i - 3] + 1
        else:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(dp[N])
    
    