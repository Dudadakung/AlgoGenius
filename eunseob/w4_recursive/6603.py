import sys

print = sys.stdout.write
input = sys.stdin.readline

used = [False for _ in range(12)]


def recursion(idx, cnt):
    if cnt == 6:
        print_answer()
    elif idx >= k:
        return
    else:
        used[idx] = True
        recursion(idx + 1, cnt + 1)
        used[idx] = False
        recursion(idx + 1, cnt)


def print_answer():
    for i in range(len(S)):
        if used[i]:
            print(S[i] + " ")
    print("\n")


S = input().split()
k = int(S.pop(0))

while k != 0:
    recursion(0, 0)
    S = input().split()
    k = int(S.pop(0))
    print("\n")
