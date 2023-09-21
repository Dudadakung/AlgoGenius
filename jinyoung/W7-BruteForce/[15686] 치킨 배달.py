from sys import stdin
from collections import deque
import math

global ans

def select_chicken(idx, num):
    global ans
    is_live[idx] = True
    live_chickens.append(chickens[idx])
    if num >= M:
        cur_dist = 0
        for house in houses:
            house_min = 99
            for chicken in live_chickens:
                house_min = min(house_min, (abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])))
            cur_dist += house_min
        ans = min(ans, cur_dist)
    else:
        for i in range(idx + 1, len(chickens)):
            if not is_live[i]:
                select_chicken(i, num + 1)
                is_live[i] = False
                live_chickens.pop()

N, M = map(int, stdin.readline().split())
city = []
houses = []
chickens = []
ans = 99999999

for _ in range(N):
    city.append(list(map(int, stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([j+1, i+1])
        elif city[i][j] == 2:
            chickens.append([j+1, i+1])

is_live = [False for _ in range(len(chickens))]

for i in range(len(chickens) - M + 1):
    live_chickens = deque()
    select_chicken(i,1)

print(ans)