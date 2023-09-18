# 2023/09/18
from sys import stdin
global cur_sum

def find_position(n):
    x = int(n / (N-2)) + 1
    y = n % (N - 2) + 1
    return [x, y]

def use_garden(x, y):
    global cur_sum
    for nx, ny in (x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        is_use[ny][nx] = True
        cur_sum += garden[ny][nx]

def un_use_garden(x, y):
    global cur_sum
    for nx, ny in (x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        is_use[ny][nx] = False
        cur_sum -= garden[ny][nx]
        
N = int(input())
garden = []
ans = 5001
is_use = [[False for _ in range(N)] for i in range(N)]
cur_sum = 0

for _ in range(N):
    garden.append(list(map(int, stdin.readline().split())))

for i in range(pow(N-2, 2)):
    i_position = find_position(i)
    use_garden(i_position[0], i_position[1])
    for j in range(i, pow(N-2, 2)):
        j_position = find_position(j)
        if not is_use[j_position[1] - 1][j_position[0]] and not is_use[j_position[1]][j_position[0] - 1]:
            use_garden(j_position[0], j_position[1])
            for k in range(j, pow(N-2, 2)):
                k_position = find_position(k)
                if not is_use[k_position[1] - 1][k_position[0]] and not is_use[k_position[1]][k_position[0] - 1]:
                    use_garden(k_position[0], k_position[1])
                    if ans > cur_sum:
                        ans = cur_sum
                    un_use_garden(k_position[0], k_position[1])
            un_use_garden(j_position[0], j_position[1])
    un_use_garden(i_position[0], i_position[1])
        
print(ans)