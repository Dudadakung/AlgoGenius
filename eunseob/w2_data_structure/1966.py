from collections import deque

q = deque()
T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    q_input = input().split()

    M = N - M - 1

    for i in q_input:
        q.appendleft(int(i))

    while True:
        num = q.pop()
        popable = True

        if q.__len__() == 0:
            break
    

        for j in q:
            if j > num:
                popable = False
                break

        if not popable:
            q.appendleft(num)
            if M == q.__len__() - 1:
                M = 0
            else:
                M += 1
        elif M == q.__len__():
            break

    print(N - q.__len__())

    q.clear()
    q_input.clear()


"""           M A
1 1 9 1 1 1   0 0
1 9 1 1 1 1   5 0
9 1 1 1 1 1   4 0
1 1 1 1 1     3 1
1 1 1 1       2 2
1 1 1         1 3
1 1           0 4
"""
