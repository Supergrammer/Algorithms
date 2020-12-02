from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
Ry, Rx, Rd = map(int, input().split())
Dy, Dx, Dd = map(int, input().split())
Ry -= 1; Rx -= 1; Rd -= 1
Dy -= 1; Dx -= 1; Dd -= 1

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]

def turn(toLeft, d):
    if toLeft:
        if d < 2: return 3 - d
        else: return d - 2
    else:
        if d < 2: return d + 2
        else: return 3 - d

def check(y, x, d):
    if 0 <= y < M and 0 <= x < N and Map[y][x] != 1:
        return True
    return False

def find():
    Q = deque([[Ry, Rx, Rd]])
    visited[Ry][Rx][Rd] = True

    time = 0
    while Q:
        size = len(Q)
        time += 1
        for _ in range(size):
            y, x, d = Q.popleft()

            for i in range(1, 4):
                iy, ix = y + dir[d][0] * i, x + dir[d][1] * i
                if check(iy, ix, d):
                    if visited[iy][ix][d]: continue
                    visited[iy][ix][d] = True
                    Q.append([iy, ix, d])
                    if iy == Dy and ix == Dx and d == Dd:
                        return time
                else: break
            for isLeft in [True, False]:
                id = turn(isLeft, d)
                if check(y, x, id):
                    if visited[y][x][id]: continue
                    visited[y][x][id] = True
                    Q.append([y, x, id])
                    if y == Dy and x == Dx and id == Dd:
                        return time

if Ry == Dy and Rx == Dx and Rd == Dd:
    print(0)
else: print(find())