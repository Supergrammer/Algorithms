import sys
input = sys.stdin.readline

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
dir = [[0, -1], [1, 0], [0, 1], [-1, 0]]

storm = [[[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 0, 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]]
storm.append([[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 0, 10, 0], [0, 0, 5, 0, 0]])
storm.append([list(reversed(storm[0][4 - i][:])) for i in range(5)])
storm.append([list(reversed(storm[1][4 - i][:])) for i in range(5)])

answer = 0

def sharkstorm(y, x, d):
    sand = Map[y][x]
    Map[y][x] = 0

    out = 0
    global answer

    def check(y, x):
        if 0 <= y < N and 0 <= x < N:
            return True
        return False

    spare = 0
    for i in range(5):
        for j in range(5):
            if storm[d][i][j] == 0:
                continue

            iy, ix = y - 2 + i, x - 2 + j
            tmp = int(sand * storm[d][i][j] / 100)
            spare += tmp

            if check(iy, ix):
                Map[iy][ix] += tmp
            else:
                out += tmp

    iy, ix = y + dir[d][0], x + dir[d][1]
    if check(iy, ix):
        Map[iy][ix] += sand - spare
    else:
        out += sand - spare

    answer += out

def move():
    ny, nx, nd = N // 2, N // 2, 0
    dist = 0

    while True:
        dist += 1
        for _ in range(2):
            for _ in range(dist):
                ny += dir[nd][0]; nx += dir[nd][1]
                if 0 <= ny < N and 0 <= nx < N:
                    sharkstorm(ny, nx, nd)
                else: return
            nd = (nd + 1) % 4

move()
print(answer)
