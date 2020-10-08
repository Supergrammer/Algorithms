import sys
input = sys.stdin.readline

N = int(input())
Map = []
mx = 0

for _ in range(N):
    Map.append(list(map(int, input().split())))

def nonzero(arr):
    return list(filter(lambda x:x!=0, arr))

def move(arr, depth):
    if depth == 5:
        global mx
        for i in range(N):
            for j in range(N):
                mx = max(mx, arr[i][j])
        return

    up, down = [[] for _ in range(N)], [[] for _ in range(N)]
    left, right = [], []

    for i in range(N):
        udtmp, lrtmp = [], []
        for j in range(N):
            udtmp.append(arr[j][i])
        udtmp = nonzero(udtmp)
        lrtmp = nonzero(arr[i][:])

        for j in range(len(udtmp) - 1):
            if udtmp[j] != 0 and udtmp[j] == udtmp[j + 1]:
                udtmp[j] *= 2; udtmp[j + 1] = 0
        udtmp = nonzero(udtmp)

        for j in range(len(lrtmp) - 1):
            if lrtmp[j] != 0 and lrtmp[j] == lrtmp[j + 1]:
                lrtmp[j] *= 2; lrtmp[j + 1] = 0
        lrtmp = nonzero(lrtmp)

        if len(udtmp) < N:
            uptmp = udtmp + ([0] * (N - len(udtmp)))
            downtmp = ([0] * (N - len(udtmp))) + udtmp
        if len(lrtmp) < N:
            lefttmp = lrtmp + ([0] * (N - len(lrtmp)))
            righttmp = ([0] * (N - len(lrtmp))) + lrtmp

        for j in range(N):
            up[j].append(uptmp[j])
            down[j].append(downtmp[j])
        left.append(lefttmp)
        right.append(righttmp)

    movarr = [up, down, left, right]

    for mov in movarr:
        move(mov, depth + 1)

move(Map, 0)
print(mx)