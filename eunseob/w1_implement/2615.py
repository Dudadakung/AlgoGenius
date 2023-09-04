def search(r, c, color):
    if (not visit_v[r][c]) and search_v(r, c, color):
        if color is black:
            print(1)
        else:
            print(2)
        print(str(r) + " " + str(c))
        exit(0)
    if (not visit_h[r][c]) and search_h(r, c, color):
        if color is black:
            print(1)
        else:
            print(2)
        print(str(r) + " " + str(c))
        exit(0)
    if (not visit_dr[r][c]) and search_dr(r, c, color):
        if color is black:
            print(1)
        else:
            print(2)
        print(str(r) + " " + str(c))
        exit(0)
    if (not visit_dl[r][c]) and search_dl(r, c, color):
        if color is black:
            print(1)
        else:
            print(2)
        print(str(r + 4) + " " + str(c - 4))
        exit(0)
    visit_v[r][c] = True
    visit_h[r][c] = True
    visit_dr[r][c] = True
    visit_dl[r][c] = True


def search_v(r, c, color):
    count = 1
    for i in range(1, 20 - r):
        if board[r + i][c] != color:
            break
        else:
            visit_v[r + i][c] = True
            count += 1

    if count == 5:
        return True
    else:
        return False


def search_h(r, c, color):
    count = 1
    for i in range(1, 20 - c):
        if board[r][c + i] != color:
            break
        else:
            visit_h[r][c + i] = True
            count += 1

    if count == 5:
        return True
    else:
        return False


def search_dr(r, c, color):
    count = 1
    m = r
    if c > r:
        m = c
    for i in range(1, 20 - m):
        if board[r + i][c + i] != color:
            break
        else:
            visit_dr[r + i][c + i] = True
            count += 1

    if count == 5:
        return True
    else:
        return False


def search_dl(r, c, color):
    count = 1
    m = c
    if 20 - r < c:
        m = 20 - r
    for i in range(1, m):
        if board[r + i][c - i] != color:
            break
        else:
            visit_dl[r + i][c - i] = True
            count += 1

    if count == 5:
        return True
    else:
        return False


board = [[0] * 20 for _ in range(20)]
visit_v = [[False] * 20 for _ in range(20)]
visit_h = [[False] * 20 for _ in range(20)]
visit_dr = [[False] * 20 for _ in range(20)]
visit_dl = [[False] * 20 for _ in range(20)]
black = 1
white = 2

for r in range(1, 20):
    line = input().split()
    for c in range(1, 20):
        board[r][c] = int(line[c - 1])

for r in range(1, 20):
    for c in range(1, 20):
        if board[r][c] == black:
            search(r, c, black)
        elif board[r][c] == white:
            search(r, c, white)
        else:
            continue

print(0)
