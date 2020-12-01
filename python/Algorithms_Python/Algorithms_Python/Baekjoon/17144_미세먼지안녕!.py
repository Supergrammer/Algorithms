import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(R)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def find():
	for i in range(R):
		for j in range(C):
			if Map[i][j] == -1:
				return (i, i + 1)

def check(y, x):
	if 0 <= y < R and 0 <= x < C and Map[y][x] != -1:
		return True
	return False

def spread():
	tmp = [[0] * C for _ in range(R)]
	for i in range(R):
		for j in range(C):
			if Map[i][j] != 0:
				if Map[i][j] == -1:
					tmp[i][j] = -1
					continue

				dust = Map[i][j]
				for dy, dx in dir:
					iy, ix = i + dy, j + dx
					if check(iy, ix):
						tmp[iy][ix] += Map[i][j] // 5
						dust -= Map[i][j] // 5
				tmp[i][j] += dust
	return tmp

def move():
	for i in range(circulator[0] - 1, 0, -1):
		Map[i][0] = Map[i - 1][0]
	for i in range(C - 1):
		Map[0][i] = Map[0][i + 1]
	for i in range(circulator[0]):
		Map[i][C - 1] = Map[i + 1][C - 1]
	for i in range(C - 1, 0, -1):
		Map[circulator[0]][i] = Map[circulator[0]][i - 1]
	
	for i in range(circulator[1] + 1, R - 1):
		Map[i][0] = Map[i + 1][0]
	for i in range(0, C - 1):
		Map[R - 1][i] = Map[R - 1][i + 1]
	for i in range(R - 1, circulator[1], -1):
		Map[i][C - 1] = Map[i - 1][C - 1]
	for i in range(C - 1, 0, -1):
		Map[circulator[1]][i] = Map[circulator[1]][i - 1]

	Map[circulator[0]][1], Map[circulator[1]][1] = 0, 0

circulator = find()
time = 0
while time != T:
	Map = spread()
	move()
	time += 1

answer = sum([sum(Map[i]) for i in range(R)]) + 2
print(answer)