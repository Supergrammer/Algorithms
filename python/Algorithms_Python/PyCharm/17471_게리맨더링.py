from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dist = [0] + list(map(int, input().split()))
Map = [[]] + [list(map(int, input().split()))[1:] for _ in range(N)]

area = [0] * (N + 1)
answer = sys.maxsize

def getarr():
    arr = [[], []]
    for i in range(1, N + 1):
        arr[area[i]].append(i)
    return arr

def calcarea():
    arr = [0, 0]
    global answer

    for i in range(1, N + 1):
        arr[area[i]] += dist[i]

    answer = min(abs(arr[0] - arr[1]), answer)

def gerrymandering(dep = 1):
    if dep == N + 1:
        arr = getarr()
        if isonearea(arr[0]) and isonearea(arr[1]):
            calcarea()
        return

    gerrymandering(dep + 1)
    area[dep] = 1
    gerrymandering(dep + 1)
    area[dep] = 0

def isonearea(arr:[]):
    if not arr:
        return False
    if len(arr) == 1:
        return True

    Q = deque([arr[0]])
    visited = [False] * (N + 1)
    visited[arr[0]] = True
    cnt = 1

    while Q:
        n = Q.popleft()
        for i in Map[n]:
            if not visited[i] and area[i] == area[n]:
                visited[i] = True
                Q.append(i)
                cnt += 1

    if cnt != len(arr):
        return False
    return True

gerrymandering()
print(-1 if answer == sys.maxsize else answer)