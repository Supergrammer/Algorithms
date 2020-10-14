from collections import deque
import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())
Map = []
smellMap = [[0] * N for _ in range(N)]
direction = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]
sharks = {}
smell = [deque([]) for _ in range(M + 1)]
sharkpriority = [[]]
time = 0

def init():
    for _ in range(N):
        Map.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if Map[i][j] != 0:
                sharks[Map[i][j]] = [i, j]
                smellMap[i][j] = Map[i][j]
                smell[Map[i][j]].append([i, j])

    tmp = list(map(int, input().split()))
    for i in range(M):
        sharks[i + 1].append(tmp[i])

    for i in range(M):
        shark = [[]]
        for j in range(4):
            tmp = list(map(int, input().split()))
            shark.append(tmp)
        sharkpriority.append(shark)

def check(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    return False

def move():
    cpyMap = [[0] * N for _ in range(N)]
    moved = []

    for i in range(1, M + 1):
        if not sharks.get(i):
            continue

        possible = []
        y, x, d = sharks[i]
        nxt = []

        for j in range(1, 5):
            iy, ix = y + direction[j][0], x + direction[j][1]
            if check(iy, ix) and smellMap[iy][ix] == 0:
                possible.append([iy, ix, j])

        if not possible:
            for j in range(1, 5):
                iy, ix = y + direction[j][0], x + direction[j][1]
                if check(iy, ix) and smellMap[iy][ix] == i:
                    possible.append([iy, ix, j])

        for j in range(4):
            id = sharkpriority[i][d][j]
            for k in range(len(possible)):
                if possible[k][2] == id:
                    d = id; nxt = possible[k]
                    break
            if nxt:
                break

        if not cpyMap[nxt[0]][nxt[1]]:
            cpyMap[nxt[0]][nxt[1]] = i
            smell[i].append([nxt[0], nxt[1]])
            sharks[i] = [nxt[0], nxt[1], id]
            moved.append(i)
        else:
            del sharks[i]
            continue

    for shark in moved:
        smellMap[sharks[shark][0]][sharks[shark][1]] = shark

    global Map
    Map = cpyMap

def deletesmell():
    for i in range(1, M + 1):
        if smell[i]:
            delete = smell[i].popleft()
            if delete in smell[i]:
                continue
            smellMap[delete[0]][delete[1]] = 0

init()
while True:
    time += 1
    move()
    if time >= k:
        deletesmell()
    if len(sharks) == 1:
        break
    if time >= 1000:
        time = -1
        break
print(time)