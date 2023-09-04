N, L = map(int, input().split())

leak = list(map(int, input().split()))

leak.sort()

count = 0
cur = leak[0]
for i in range(N):
    if leak[i] < cur:
        continue
    cur = leak[i] + L
    count += 1

print(count)
