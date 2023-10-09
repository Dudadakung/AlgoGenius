import sys

print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
field = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
cost_list = []

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        field[i][j] = row[j - 1]


def calculate(px, py):
    return (
        field[px + 1][py]
        + field[px - 1][py]
        + field[px][py + 1]
        + field[px][py - 1]
        + field[px][py]
    )


def can_blossom(x1, y1, x2, y2):
    if (abs(x1 - x2) + abs(y1 - y2)) > 2:
        return True
    else:
        return False


for x1 in range(2, N):
    for y1 in range(2, N):
        for x2 in range(2, N):
            for y2 in range(2, N):
                if can_blossom(x1, y1, x2, y2):
                    for x3 in range(2, N):
                        for y3 in range(2, N):
                            if can_blossom(x1, y1, x3, y3) and can_blossom(
                                x2, y2, x3, y3
                            ):
                                cost_list.append(
                                    calculate(x1, y1)
                                    + calculate(x2, y2)
                                    + calculate(x3, y3)
                                )


print(str(min(cost_list)))
