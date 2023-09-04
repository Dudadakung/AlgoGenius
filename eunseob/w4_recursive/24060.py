import sys

input = sys.stdin.readline


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    global count
    i, j, t = p, q + 1, 1
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = arr[i]
        t += 1
        i += 1

    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1

    i = p
    t = 1
    while i <= r:
        arr[i] = tmp[t]
        count += 1
        if count == K:
            print(arr[i])
            exit(0)
        i += 1
        t += 1


count = 0
N, K = map(int, input().split())
A = list(map(int, input().split()))
tmp = [0 for _ in range(N + 1)]
merge_sort(A, 0, N - 1)
print(-1)
