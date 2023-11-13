from sys import stdin

def solve():
    position = 0
    ans = 0
    cur = set()

    for i in range(K):
        cur.add(belt[i])
        chobab_count[belt[i]] += 1
        
    while N > position:
        if not C in cur:
            ans = max(ans, len(cur) + 1)
        else:
            ans = max(ans, len(cur))

        chobab_count[belt[position]] -= 1
        if chobab_count[belt[position]] == 0:
            cur.remove(belt[position])
        
        chobab_count[belt[(position + K) % N]] += 1
        cur.add(belt[(position + K) % N])

        position += 1
        
    return ans
    

N, D, K, C = map(int, stdin.readline().split())

belt = []
chobab_count = [0 for _ in range(D + 1)]

for _ in range(N):
    belt.append(int(stdin.readline()))

ans = solve()

print(ans)