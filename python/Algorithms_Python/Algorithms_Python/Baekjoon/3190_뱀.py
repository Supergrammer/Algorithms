from collections import deque
import sys
input = sys.stdin.readline

def move():
	y, x = snake[-1]
	dy, dx = dir[d]
	iy, ix = y + dy, x + dx
	if not check(iy, ix):
		return False

	y, x = iy, ix
	snake.append([y, x])
	if not Map[y][x]:
		snake.popleft()
	else:
		Map[y][x] = 0

	if rotArr and rotArr[0][0] == time:
		rotate(rotArr[0][1])
		rotArr.pop(0)
	return True

def check(iy, ix):
	if 0 <= iy < N and 0 <= ix < N and \
		not snake.count([iy, ix]):
		return True
	return False

def rotate(C):
	global d
	if C == 'L': d = (d + 3) % 4
	else: d = (d + 1) % 4

N = int(input())
K = int(input())
Map = [[0 for x in range(N)] for y in range(N)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
snake = deque([[0, 0]])
time, d = 0, 0

for _ in range(K):
	y, x = map(int, input().split())
	Map[y - 1][x - 1] = 1

L = int(input())
rotArr = []

for _ in range(L):
	X, C = input().split()
	rotArr.append([int(X), C])

rotArr.sort()

while True:
	time += 1
	if not move():
		print(time)
		break