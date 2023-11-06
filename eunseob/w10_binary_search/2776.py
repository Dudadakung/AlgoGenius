import sys

print = sys.stdout.write
input = sys.stdin.readline


def binary_search(n, note):
    result = "0"

    mn = 0
    mx = N - 1
    while True:
        if mx == mn or mx == mn + 1:
            if note[mx] == n or note[mn] == n:
                result = "1\n"
                break
            else:
                result = "0\n"
                break

        mid = (mx + mn) // 2
        if note[mid] < n:
            mn = mid
        else:
            mx = mid

    return result


T = int(input())

for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()

    M = int(input())
    note2 = list(map(int, input().split()))

    for n in note2:
        print(binary_search(n, note1))
