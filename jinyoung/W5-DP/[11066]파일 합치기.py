# 2023/09/07
from sys import stdin
from copy import deepcopy

T = int(stdin.readline())

while T > 0:
    T -= 1
    K = int(stdin.readline())
    books = list(map(int, stdin.readline().split()))
    
    dp = [[0 for _ in range(K)] for i in range(K)]
    dp_sum = []
    
    dp[0] = books

    while 1:
        for i in range(1, K - 1):
            for book_num in range(0, K - i):
                dp[i][book_num] = dp[i - 1][book_num] + dp[0][book_num + i]

        dp_sum = deepcopy(dp)
        for i in range(2, K - 1):
            for book_num in range(0, K - i):
                dp_sum[i][book_num] += dp_sum[i - 1][book_num]
        dp_sum[0] = [0 for _ in range(K)]
        ans = 999999999999999999999
        
        for i in range(K - 2, int(K/2) - 2, -1):
            for book_num in range(0, K - i):
                if book_num + i + 1 < i + 2:
                    ans = min(dp[i][book_num] + dp[K - i - 2][(book_num + i + 1)] + dp_sum[i][book_num]+ dp_sum[K - i - 2][(book_num + i + 1)],ans)
                if book_num - K - i - 1 >= 0:
                    ans = min(dp[i][book_num] + dp[K - i - 2][(book_num - K - i - 1)] + dp_sum[i][book_num]+ dp_sum[K - i - 2][(book_num - K - i - 1)],ans)

        break
        1

    print(ans)
    
