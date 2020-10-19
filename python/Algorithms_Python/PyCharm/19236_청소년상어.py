import sys
input = sys.stdin.readline

Map = [[[] for _ in range(4)] for _ in range(4)]
direction = [[], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

fishes = [[] for _ in range(17)]
answer = 0

def init():
    for i in range(4):
        tmp = list(map(int, input().split()))
        for j in range(4):
            Map[i][j] = [tmp[j * 2], tmp[j * 2 + 1]]
            fishes[tmp[j * 2]] = [i, j]

def check(ny, nx):
    if 0 <= ny < 4 and 0 <= nx < 4:
        return True
    return False

def move(Map, fishes):
    for i in range(1, 17):
        if fishes[i]:
            y, x = fishes[i]
            d = Map[y][x][1]

            while True:
                ny, nx = y + direction[d][0], x + direction[d][1]
                if check(ny, nx)\
                        and (not Map[ny][nx] or Map[ny][nx][0] != 0):
                    break
                else:
                    d += 1
                    if d > 8: d -= 8

            fishes[i] = [ny, nx]
            if Map[ny][nx]:
                fishes[Map[ny][nx][0]] = [y, x]
            Map[y][x], Map[ny][nx] = Map[ny][nx], Map[y][x]
            Map[ny][nx][1] = d

    return Map, fishes

def turn(Map, fishes, y, x, score):
    cpyMap = [[block[:] for block in row] for row in Map]
    cpyfishes = [row[:] for row in fishes]

    cpyfishes[cpyMap[y][x][0]] = []
    score += cpyMap[y][x][0]
    if cpyfishes[0]:
        cpyMap[cpyfishes[0][0]][cpyfishes[0][1]] = []
    cpyfishes[0] = [y, x]
    cpyMap[y][x][0] = 0

    cpyMap, cpyfishes = move(cpyMap, cpyfishes)

    d = cpyMap[y][x][1]
    nxt = []
    while True:
        y += direction[d][0]; x += direction[d][1]
        if check(y, x):
            if cpyMap[y][x]:
                nxt.append([y, x])
        else: break

    if not nxt:
        global answer
        answer = max(score, answer)
        return

    for iy, ix in nxt:
        turn(cpyMap, cpyfishes, iy, ix, score)

init()
turn(Map, fishes, 0, 0, 0)
print(answer)