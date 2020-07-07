import sys
input = sys.stdin.readline

def move(d):
	global y, x, top
	iy = y + dir[d][0]; ix = x + dir[d][1]

	if not check(iy, ix):
		return

	rotate(d)
	
	y, x = iy, ix
	if Map[y][x] == 0:
		Map[y][x] = dice[0][7 - dice[1][0]]
	else:
		dice[0][7 - dice[1][0]] = Map[y][x]
		Map[y][x] = 0

	print(dice[0][dice[1][0]])

def rotate(d):
	if d in [1, 2]:
		if d == 1: dice[1] = [dice[1][-1]] + dice[1][:-1]
		else: dice[1] = dice[1][1:] + [dice[1][0]]
		dice[2][0], dice[2][2] = dice[1][0], dice[1][2]
	else:
		if d == 3: dice[2] = dice[2][1:] + [dice[2][0]]
		else: dice[2] = [dice[2][-1]] + dice[2][:-1]
		dice[1][0], dice[1][2] = dice[2][0], dice[2][2]

def check(iy, ix):
	if 0 <= iy < N and 0 <= ix < M:
		return True
	return False

dice = [[0, 0, 0, 0, 0, 0, 0], [1, 3, 6, 4], [1, 5, 6, 2]]
dir = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
Map = []

N, M, x, y, K = map(int, input().split())
for _ in range(N):
	Map.append(list(map(int, input().split())))
MovDir = map(int, input().split())

for d in MovDir:
	move(d)