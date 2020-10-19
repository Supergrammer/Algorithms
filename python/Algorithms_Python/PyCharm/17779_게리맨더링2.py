import sys
input = sys.stdin.readline

N = int(input())
Map = [[]]
answer = sys.maxsize

for _ in range(N):
    Map.append([0] + list(map(int, input().split())))

def gerrymandering(x, y, d1, d2):
    p1, p2, row = 0, 0, 0
    isFifth = [[False] * (N + 1) for _ in range(N + 1)]
    ward = [0] * 5

    for i in range(x, x + d1 + d2 + 1):
        for j in range(y - p1, y + p2 + 1):
            ward[4] += Map[i][j]
            isFifth[i][j] = True

        p1 += (1 if row < d1 else -1)
        p2 += (1 if row < d2 else -1)
        row += 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not isFifth[i][j]:
                if 1 <= i < x + d1 and 1 <= j <= y: ward[0] += Map[i][j]
                elif 1 <= i <= x + d2 and y < j <= N: ward[1] += Map[i][j]
                elif x + d1 <= i <= N and 1 <= j < y - d1 + d2: ward[2] += Map[i][j]
                else: ward[3] += Map[i][j]

    global answer
    answer = min(answer, max(ward) - min(ward))

for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, y):
            if y - d1 < 1: continue
            for d2 in range(1, N - y + 1):
                if x + d1 + d2 > N or y + d2 > N: continue
                gerrymandering(x, y, d1, d2)

print(answer)