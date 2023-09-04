def rotate():
    temp = belt[2 * N - 1]
    for i in range(2 * N - 2, -1, -1):
        belt[i + 1] = belt[i]
        if (i < N - 1) and robot_state[i]:
            robot_state[i] = False
            robot_state[i + 1] = True
            if i + 1 == N - 1:
                robot_state[N - 1] = False
    belt[0] = temp
    if robot_state[0]:
        robot_state[0] = False
        robot_state[1] = True
        if N == 2:
            robot_state[N - 1] = False


def robot_move():
    bc = 0
    for i in range(N - 2, -1, -1):
        if robot_state[i] and (not robot_state[i + 1]) and (belt[i + 1] != 0):
            belt[i + 1] -= 1
            robot_state[i] = False
            robot_state[i + 1] = True
            if belt[i + 1] == 0:
                bc += 1
            if i + 1 == N - 1:
                robot_state[N - 1] = False

    return bc


def add_robot():
    bc = 0
    if belt[0] != 0:
        robot_state[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            bc += 1

    return bc


N, K = map(int, input().split())

broken = 0
count = 0
belt = [0 for _ in range(2 * N)]
robot_state = [False for _ in range(N)]

dur = input().split()
for i in range(2 * N):
    belt[i] = int(dur[i])
    if belt[i] == 0:
        broken += 1

# 대충 한번 돌 때 400
while True:
    count += 1
    rotate()
    broken += robot_move()
    broken += add_robot()
    if broken >= K:
        print(count)
        exit(0)
