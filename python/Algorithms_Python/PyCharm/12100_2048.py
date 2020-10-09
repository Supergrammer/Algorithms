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
        utmp, dtmp, ltmp, rtmp = [], [], nonzero(arr[i][:]), nonzero((arr[i][:]))
        for j in range(N):
            utmp.append(arr[j][i])
            dtmp.append(arr[j][i])
        utmp = nonzero(utmp)
        dtmp = nonzero(dtmp)

        for j in range(len(utmp) - 1):
            if utmp[j] != 0 and utmp[j] == utmp[j + 1]:
                utmp[j] *= 2; utmp[j + 1] = 0
        utmp = nonzero(utmp)

        for j in range(len(dtmp) - 1, 0, -1):
            if dtmp[j] != 0 and dtmp[j] == dtmp[j - 1]:
                dtmp[j] *= 2; dtmp[j - 1] = 0
        dtmp = nonzero(dtmp)

        for j in range(len(ltmp) - 1):
            if ltmp[j] != 0 and ltmp[j] == ltmp[j + 1]:
                ltmp[j] *= 2; ltmp[j + 1] = 0
        ltmp = nonzero(ltmp)

        for j in range(len(rtmp) - 1, 0, -1):
            if rtmp[j] != 0 and rtmp[j] == rtmp[j - 1]:
                rtmp[j] *= 2; rtmp[j - 1] = 0
        rtmp = nonzero(rtmp)

        utmp = utmp + ([0] * (N - len(utmp)))
        dtmp = ([0] * (N - len(dtmp))) + dtmp
        ltmp = ltmp + ([0] * (N - len(ltmp)))
        rtmp = ([0] * (N - len(rtmp))) + rtmp

        for j in range(N):
            up[j].append(utmp[j])
            down[j].append(dtmp[j])
        left.append(ltmp)
        right.append(rtmp)

    movarr = [up, down, left, right]

    for mov in movarr:
        move(mov, depth + 1)

move(Map, 0)
print(mx)