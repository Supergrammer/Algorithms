import sys
input = sys.stdin.readline

Map = [[[] for _ in range(4)] for _ in range(4)]
direction = [[], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

fishes = [[] for _ in range(17)]
answer = 0

def ipt():
    for i in range(4):
        tmp = list(map(int, input().split()))
        for j in range(4):
            Map[i][j] = [tmp[j * 2], tmp[j * 2 + 1]]
            fishes[tmp[j * 2]] = [i, j, tmp[j * 2 + 1]]

def init():
    global answer
    fishes[0] = [0, 0, Map[0][0][1]]
    fishes[Map[0][0][0]] = []
    answer += Map[0][0][0]
    Map[0][0][0] = 0

def check(ny, nx):
    if 0 <= ny < 4 and 0 <= nx < 4\
            and (not Map[ny][nx] or Map[ny][nx][0] != 0):
        return True
    return False

def move(Map, fishes):
    for i in range(1, 17):
        if fishes[i]:
            y, x, d = fishes[i]
            ny, nx = 0, 0

            while True:
                ny, nx = y + direction[d][0], x + direction[d][1]
                if check(ny, nx):
                    break
                else:
                    d += 1
                    if d > 8: d -= 8

            fishes[i] = [ny, nx, d]
            if Map[ny][nx]:
                fishes[Map[ny][nx][0]][0], fishes[Map[ny][nx][0]][1] = y, x
            Map[y][x][1] = d
            Map[y][x], Map[ny][nx] = Map[ny][nx], Map[y][x]
    return Map, fishes

def copy(Map, fishes):
    cpyMap = [[[] for _ in range(4)] for _ in range(4)]
    cpyfishes = [[] for _ in range(17)]

    for i in range(4):
        for j in range(4):
            cpyMap[i][j] = Map[i][j][:]
    for i in range(17):
        cpyfishes[i] = fishes[i][:]

    return cpyMap, cpyfishes

def shark(Map, fishes, fishscore):
    cpyMap, cpyfishes = copy(Map, fishes)
    cpyMap, cpyfishes = move(cpyMap, cpyfishes)

    y, x = fishes[0][0], fishes[0][1]
    ischanged = False

    t = 1
    while True:
        iy = y + direction[fishes[0][2]][0] * t
        ix = x + direction[fishes[0][2]][1] * t
        if not check(iy, ix):
             break
        t += 1
        if not Map[iy][ix]:
            continue

        ischanged = True
        recMap, recfishes = copy(cpyMap, cpyfishes)

        recfishes[0] = [iy, ix, recMap[iy][ix][1]]
        recfishes[recMap[iy][ix][0]] = []
        score = fishscore + recMap[iy][ix][0]
        recMap[iy][ix] = [0, recfishes[0][2]]
        recMap[y][x] = []

        shark(recMap, recfishes, score)

    if not ischanged:
        global answer
        answer = max(answer, fishscore)

ipt()
init()
shark(Map, fishes, answer)

print(answer)