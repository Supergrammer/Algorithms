from collections import deque
import sys
input = sys.stdin.readline

Green = deque([[0] * 4 for _ in range(6)])
Blue = deque([[0] * 4 for _ in range(6)])

N = int(input())
score = 0

def blockDown(arr:[], Map:[], t):
    line = -1
    for i in range(6):
        isEmpty = True
        for j in arr:
            if Map[i][j] == 1:
                isEmpty = False
        if not isEmpty:
            line = i - 1
            break

    for i in arr:
        Map[line][i] = 1
    if (t == 3 and Map == Green) or (t == 2 and Map == Blue):
        Map[line - 1][arr[0]] = 1

def getScore(Map:[]):
    isDeleted = []
    global score

    for i in range(5, 1, -1):
        isFull = True
        for j in range(4):
            if Map[i][j] == 0:
                isFull = False; break
        if isFull:
            isDeleted.append(i)
            score += 1

    for i in isDeleted:
        del Map[i]

    if isDeleted:
        for _ in isDeleted:
            Map.appendleft([0] * 4)

def goDown(Map:[]):
    cnt = 0
    for i in range(2):
        isBlock = False
        for j in range(4):
            if Map[i][j] == 1:
                isBlock = True; break

        if isBlock: cnt += 1

    if cnt:
        for _ in range(cnt):
            Map.pop()
            Map.appendleft([0] * 4)

def getBlock():
    block = 0
    for Map in [Green, Blue]:
        for i in range(6):
            for j in range(4):
                block += Map[i][j]
    return block

for _ in range(N):
    t, y, x = map(int, input().split())
    blockDown([x] + ([x + 1] if t == 2 else []), Green, t)
    blockDown([3 - y] + ([2 - y] if t == 3 else []), Blue, t)

    for Map in [Green, Blue]:
        getScore(Map)
        goDown(Map)

print(score)
print(getBlock())