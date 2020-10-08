from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
Map = [[0] * N for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    Map[y - 1][x - 1] = 2

L = int(input())
change = []
for _ in range(L):
    tmp = list(input().split())
    tmp[0] = int(tmp[0])
    change.append(tmp)
pointer = 0

Map[0][0] = 1
snake, d = deque([[0, 0]]), 1
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def check(y, x):
    if not (0 <= y < N and 0 <= x < N) or Map[y][x] == 1:
        return False
    return True

def move(t):
    global pointer
    if pointer < len(change) and t == change[pointer][0] + 1:
        global d
        if change[pointer][1] == 'L':
            d = (d + 3) % 4
        else: d = (d + 1) % 4
        pointer += 1

    y, x = snake[0][0] + dir[d][0], snake[0][1] + dir[d][1]
    if check(y, x):
        snake.appendleft([y, x])
        if Map[y][x] == 0:
            dy, dx = snake.pop()
            Map[dy][dx] = 0
        Map[y][x] = 1
        return True
    else: return False

time = 0
while True:
    time += 1
    if not move(time):
        print(time)
        break