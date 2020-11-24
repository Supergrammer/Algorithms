from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def rotate(Li):
    rotated = [[0] * 2 ** N for _ in range(2 ** N)]
    for i in range(2 ** (N - Li)):
        for j in range(2 ** (N - Li)):
            y, x = 2 ** Li * i, 2 ** Li * j
            for k in range(2 ** Li):
                for l in range(2 ** Li):
                    rotated[y + l][x + 2 ** Li - 1 - k] = Map[y + k][x + l]
    return rotated

def melt():
    melted = [[0] * 2 ** N for _ in range(2 ** N)]
    for i in range(2 ** N):
        for j in range(2 ** N):
            if Map[i][j] == 0:
                continue

            melted[i][j] = Map[i][j]
            cnt = 0
            for dy, dx in dir:
                iy, ix = i + dy, j + dx
                if 0 <= iy < 2 ** N and 0 <= ix < 2 ** N and Map[iy][ix] != 0:
                    cnt += 1

            if cnt < 3:
                melted[i][j] -= 1
    return melted

size = []
visited = [[False] * 2 ** N for _ in range(2 ** N)]

def find():
    for i in range(2 ** N):
        for j in range(2 ** N):
            if Map[i][j] != 0 and not visited[i][j]:
                Q = deque([[i, j]])
                visited[i][j] = True
                siz = 1

                while Q:
                    y, x = Q.popleft()
                    for dy, dx in dir:
                        iy, ix = y + dy, x + dx
                        if 0 <= iy < 2 ** N and 0 <= ix < 2 ** N and\
                                not visited[iy][ix] and Map[iy][ix] != 0:
                            Q.append([iy, ix])
                            visited[iy][ix] = True
                            siz += 1
                size.append(siz)

for i in range(Q):
    Map = rotate(L[i])
    Map = melt()
find()

print(sum([sum(Map[i]) for i in range(2 ** N)]))
print(max(size) if size else 0)