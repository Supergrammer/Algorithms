import sys
input = sys.stdin.readline

N = int(input())
Map = [[0] * 10 for _ in range(4)] + [[0] * 4 for _ in range(6)]
score = 0
tiles = []

def blue(y, num):
    iy = []
    located = 0
    if tiles[num - 1] == 3: iy = [y, y + 1]
    else: iy = [y]

    for i in range(4, 10):
        flag = False
        for j in iy:
            if Map[j][i] != 0:
                located = i - 1
                flag = True
        if flag: break

    if located == 0: located = 9

    Map[y][located] = num
    if tiles[num - 1] == 2: Map[y][located - 1] = num
    elif tiles[num - 1] == 3: Map[y + 1][located] = num

def green(t, num):
    ix = []
    located = 0
    if tiles[num - 1] == 2: ix = [x, x + 1]
    else: ix = [x]

    for i in range(4, 10):
        flag = False
        for j in ix:
            if Map[i][j] != 0:
                located = i - 1
                flag = True
        if flag: break

    if located == 0: located = 9

    Map[located][x] = num
    if tiles[num - 1] == 2: Map[located][x + 1] = num
    elif tiles[num - 1] == 3: Map[located - 1][x] = num

def checkBlue():
    for i in range(9, 3, -1):
        flag = True
        for j in range(4):
            if Map[j][i] == 0:
                flag = False

        if flag:
            global score
            score += 1
            for j in range(4):
                Map[j][i] = 0

            sortBlue()
            return False
    return True

def sortBlue():
    checked = [[0] * 10 for _ in range(4)]
    for i in range(9, 3, -1):
        for j in range(4):
            if Map[j][i] != 0:
                n = Map[j][i]
                if j != 3 and Map[j + 1][i] == n:
                    iy = [j, j + 1]
                else:
                    iy = [j]

                located = 0

                for l in range(4, 10):
                    flag = False
                    for m in iy:
                        if checked[m][l] != 0:
                            located = l - 1
                            flag = True
                    if flag: break

                if located == 0: located = 9

                checked[j][located] = n
                if j != 3 and Map[j + 1][i] == n:
                    checked[j + 1][located] = n
                    Map[j + 1][i] = 0
                elif Map[j][i - 1] == n:
                    checked[j][located - 1] = n
                    Map[j][i - 1] = 0

    for i in range(4):
        Map[i] = checked[i]

def checkGreen():
    for i in range(9, 3, -1):
        flag = True
        for j in range(4):
            if Map[i][j] == 0:
                flag = False

        if flag:
            global score
            score += 1
            for j in range(4):
                Map[i][j] = 0

            sortGreen()
            return False
    return True

def sortGreen():
    checked = [[0] * 4 for _ in range(6)]
    for i in range(9, 3, -1):
        for j in range(4):
            if Map[i][j] != 0:
                n = Map[i][j]
                if j != 3 and Map[i][j + 1] == n:
                    ix = [j, j + 1]
                else:
                    ix = [j]

                located = 0

                for l in range(6):
                    flag = False
                    for m in ix:
                        if checked[l][m] != 0:
                            located = l - 1
                            flag = True
                    if flag: break

                if located == 0: located = 5

                checked[located][j] = n
                if j != 3 and Map[i][j + 1] == n:
                    checked[located][j + 1] = n
                    Map[i][j + 1] = 0
                elif i != 0 and Map[i - 1][j] == n:
                    checked[located - 1][j] = n
                    Map[i - 1][j] = 0

    for i in range(6):
        Map[i + 4] = checked[i]

def checkBlueMid():
    for i in range(4):
        for j in range(4, 6):
            if Map[i][j] != 0:
                for k in range(4):
                    Map[k] = [0] + Map[k][:9]
                return False
    return True

def checkGreenMid():
    for i in range(4, 6):
        for j in range(4):
            if Map[i][j] != 0:
                for k in range(9, 4, -1):
                    Map[k] = Map[k - 1][:]
                return False
    return True

for n in range(1, N + 1):
    t, y, x = map(int, input().split())
    tiles.append(t)

    blue(y, n)
    green(x, n)

    while True:
        if checkBlueMid():
            break
    while True:
        if checkGreenMid():
            break
    while True:
        if checkBlue():
            break
    while True:
        if checkGreen():
            break

cnt = 0
for i in range(10):
    for j in Map[i]:
        if j != 0:
            cnt += 1

print(score)
print(cnt)