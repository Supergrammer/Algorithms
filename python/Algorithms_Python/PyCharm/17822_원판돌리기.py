from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
Map = []

for _ in range(N):
    Map.append(list(map(int, input().split())))

def check():
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[0] * M for _ in range(N)]
    isChanged = False

    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0 and not visited[i][j]:
                Q = deque([[i, j]])
                visited[i][j] = 1
                flag = False
                tmp = []
                while Q:
                    Y, X = Q.popleft()
                    for dy, dx in dir:
                        iy, ix = Y + dy, (X + dx) % M
                        if not 0 <= iy < N: continue
                        if not visited[iy][ix] and Map[iy][ix] == Map[Y][X]:
                            Q.append([iy, ix])
                            visited[iy][ix] = 1
                            tmp.append([iy, ix])
                            flag = True
                            isChanged = True

                for Y, X in tmp:
                    Map[Y][X] = 0
                if flag: Map[i][j] = 0
    return isChanged

def flatten():
    sm, nonzero = 0, 0
    avg = 0

    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0:
                sm += Map[i][j]
                nonzero += 1
    if nonzero == 0:
        return
    avg = sm / nonzero

    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0: continue
            if Map[i][j] < avg: Map[i][j] += 1
            elif Map[i][j] > avg: Map[i][j] -= 1

for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(N):
        if (i + 1) % x == 0:
            if d: Map[i] = Map[i][k%M:] + Map[i][:k%M]
            else: Map[i] = Map[i][(M-k)%M:] + Map[i][:(M-k)%M]

    if not check():
        flatten()

answer = 0
for i in range(N):
    for j in range(M):
        answer += Map[i][j]

print(answer)