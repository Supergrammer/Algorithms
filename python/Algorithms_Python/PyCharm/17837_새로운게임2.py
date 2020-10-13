import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tile = []
Map = [[[] for _ in range(N)] for _ in range(N)]
direction = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
pieces = []

def init():
    for _ in range(N):
        tile.append(list(map(int, input().split())))
    for i in range(K):
        y, x, d = map(int, input().split())
        Map[y - 1][x - 1].append(i + 1)
        pieces.append([y - 1, x - 1, d])

def check(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

def changeDir(d):
    if d % 2: return d + 1
    else: return d - 1

def move(i, y, x, d, tmp, isRepeated):
    ny, nx = y + direction[d][0], x + direction[d][1]
    if check(ny, nx):
        if tile[ny][nx] == 0:
            Map[ny][nx] += tmp
            for p in tmp:
                pieces[p - 1][0], pieces[p - 1][1] = ny, nx

        elif tile[ny][nx] == 1:
            Map[ny][nx] += reversed(tmp)
            for p in tmp:
                pieces[p - 1][0], pieces[p - 1][1] = ny, nx

        if tile[ny][nx] == 2:
            if isRepeated:
                Map[y][x] += tmp
                return

            pieces[i][2] = changeDir(d)
            move(i, y, x, pieces[i][2], tmp, True)
    else:
        pieces[i][2] = changeDir(d)
        move(i, y, x, pieces[i][2], tmp, True)

def turn():
    for i in range(K):
        y, x, d = pieces[i]
        tmp = []

        for j in range(len(Map[y][x])):
            if Map[y][x][j] == i + 1:
                tmp = Map[y][x][j:]
                Map[y][x] = Map[y][x][:j]
                break

        move(i, y, x, d, tmp, False)
        y, x = pieces[i][0], pieces[i][1]
        if len(Map[y][x]) >= 4:
            return True
    return False

init()
answer = 0
while True:
    answer += 1
    if turn():
        print(answer); break
    if answer > 1000:
        print(-1); break
