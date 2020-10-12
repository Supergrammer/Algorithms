import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
Map = [[0] * (C + 1) for _ in range(R + 1)]
sharks = {}
direction = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]
answer = 0

def ipt():
    for i in range(1, M + 1):
        r, c, s, d, z = map(int, input().split())
        Map[r][c] = i
        if d in [1, 2]: s %= 2 * (R - 1)
        else: s %= 2 * (C - 1)
        sharks[i] = [r, c, s, d, z]

def check(y, x):
    if 0 < y <= R and 0 < x <= C:
        return True
    return False

def catch(now):
    for i in range(1, R + 1):
        if Map[i][now] != 0:
            rtn = sharks[Map[i][now]][4]
            del sharks[Map[i][now]]
            Map[i][now] = 0
            return rtn
    return 0

def turn(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    elif d == 4: return 3

def move():
    tmp = [[0] * (C + 1) for _ in range(R + 1)]

    for i in range(1, M + 1):
        if not sharks.get(i):
            continue

        r, c, s, d, z = sharks[i]
        ny, nx = r, c

        for _ in range(s):
            ny, nx = ny + direction[d][0], nx + direction[d][1]
            if not check(ny, nx):
                d = turn(d)
                ny, nx = ny + direction[d][0] * 2, nx + direction[d][1] * 2

        r, c = ny, nx
        sharks[i] = [r, c, s, d, z]

        if tmp[r][c] != 0:
            if sharks[tmp[r][c]][4] > sharks[i][4]:
                del sharks[i]
            else:
                del sharks[tmp[r][c]]
                tmp[r][c] = i
        else: tmp[r][c] = i

    for i in range(R + 1):
        for j in range(C + 1):
            Map[i][j] = tmp[i][j]

ipt()
for i in range(1, C + 1):
    answer += catch(i)
    move()

print(answer)