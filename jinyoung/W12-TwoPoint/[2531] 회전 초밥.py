from sys import stdin

def solve():
    front = 0
    back = K - 1
    
    ans = 0
    while N > back:
        cur = set()
        i = 0
        for i in range(front, back + 1):
            cur.add(belt[i])
        if C == belt[(i + 1) % N] or C == belt[(front - 1 + N) % N]:
            if not C in cur:
                cur.add(3001)
        elif not C in cur:
            cur.add(3001)
        ans = max(ans, len(cur))
        front += 1
        back += 1
    front = N - K + 1
    back = N
    while N > front:
        cur = set()
        for i in range(front, back + 1):
            cur.add(belt[i % N])
        if C == belt[i % N + 1] or C == belt[front - 1 % N]:
            if not C in cur:
                cur.add(3001)
        elif not C in cur:
            cur.add(3001)

        ans = max(ans, len(cur))
        front += 1
        back += 1
        
    return ans
    

N, D, K, C = map(int, stdin.readline().split())

belt = []

for _ in range(N):
    belt.append(int(stdin.readline()))

ans = solve()

print(ans)