from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map = []
virus = []
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 10000
cnt = 0

def init():
    global cnt
    for _ in range(N):
        Map.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 0:
                cnt += 1
            elif Map[i][j] == 2:
                virus.append([i, j])

def search(comb):
    cpyMap = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        cpyMap.append(Map[i][:])

    Q = deque([comb[i][:] for i in range(len(comb))])
    for y, x in comb:
        visited[y][x] = True

    time, scnt = 0, 0

    while Q:
        size = len(Q); time += 1
        while size != 0:
            y, x = Q.popleft()
            size -= 1

            for dy, dx in direction:
                iy, ix = y + dy, x + dx
                if 0 <= iy < N and 0 <= ix < N\
                        and not visited[iy][ix] and cpyMap[iy][ix] != 1:
                    if cpyMap[iy][ix] == 0:
                        cpyMap[iy][ix] = 1
                        scnt += 1
                        if scnt == cnt:
                            return time
                    Q.append([iy, ix])
                    visited[iy][ix] = True
    return 10000

init()
if cnt == 0:
    print(0)
else:
    combination = combinations(virus, M)
    for comb in combination:
        answer = min(answer, search(comb))
    print(answer if answer != 10000 else -1)