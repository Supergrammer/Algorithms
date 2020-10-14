from collections import deque
import sys
input = sys.stdin.readline

N, M, fuel = map(int, input().split())
Map = []
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
driver = []
passenger = []

def init():
    for _ in range(N):
        Map.append(list(map(int, input().split())))
    global driver
    driver = list(map(int, input().split()))
    driver[0] -= 1; driver[1] -= 1
    for i in range(M):
        y, x, toy, tox = map(int, input().split())
        Map[y - 1][x - 1] = i + 2
        passenger.append([toy - 1, tox - 1, y - 1, x - 1])

def check(y, x):
    if 0 <= y < N and 0 <= x < N\
            and Map[y][x] != 1:
        return True
    return False

def findpassenger():
    if Map[driver[0]][driver[1]] > 1:
        return Map[driver[0]][driver[1]] - 2, 0

    Q = deque([driver])
    visited = [[False] * N for _ in range(N)]
    visited[driver[0]][driver[1]] = 1
    distance = 0
    tmp = []

    while Q:
        size = len(Q)
        distance += 1
        while size:
            y, x = Q.popleft()
            size -= 1

            for dy, dx in direction:
                iy, ix = y + dy, x + dx
                if check(iy, ix) and not visited[iy][ix]:
                    Q.append([iy, ix])
                    visited[iy][ix] = True
                    if Map[iy][ix] != 0:
                        tmp.append(Map[iy][ix] - 2)

        if tmp:
            tmp = sorted(tmp, key=lambda p:(passenger[p][2], passenger[p][3]))
            return tmp[0], distance
    return -1, -1

def movepassenger(p):
    Q = deque([driver])
    visited = [[False] * N for _ in range(N)]
    visited[driver[0]][driver[1]] = 1
    distance = 0

    while Q:
        size = len(Q)
        distance += 1
        while size:
            y, x = Q.popleft()
            size -= 1

            for dy, dx in direction:
                iy, ix = y + dy, x + dx
                if check(iy, ix) and not visited[iy][ix]:
                    Q.append([iy, ix])
                    visited[iy][ix] = True
                    if [iy, ix] == passenger[p][:2]:
                        return distance
    return -1

init()
for _ in range(M):
    p, d = findpassenger()
    fuel -= d
    if fuel < 0 or d == -1:
        fuel = -1; break
    driver = passenger[p][2:]
    Map[passenger[p][2]][passenger[p][3]] = 0

    d = movepassenger(p)
    fuel -= d
    if fuel < 0 or d == -1:
        fuel = -1; break
    fuel += d * 2
    driver = passenger[p][:2]

print(fuel)