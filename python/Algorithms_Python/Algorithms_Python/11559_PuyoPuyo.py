from collections import deque
import sys
input = sys.stdin.readline

def Puyo(y, x, c):
	Q = deque([[y, x]])
	tmp = [[y, x]]
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	visited[y][x] = True
	cnt = 1

	while Q:
		y, x = Q.popleft()
		for dy, dx in dir:
			iy, ix = y + dy, x + dx
			if 0 <= iy < 12 and 0 <= ix < 6 and\
				Map[iy][ix] == c and not visited[iy][ix]:
				Q.append([iy, ix])
				tmp.append([iy, ix])
				visited[iy][ix] = True
				cnt += 1

	if cnt >= 4:
		for y, x in tmp:
			Map[y][x] = '.'
		global puyo
		puyo = True

def down():
	for x in range(6):
		tmp = []
		for y in range(12):
			if Map[y][x] != '.':
				tmp.append(Map[y][x])
		tmp = list('.' * (12 - len(tmp))) + tmp
		for y in range(12):
			Map[y][x] = tmp[y]

Map = []
for _ in range(12):
	Map.append(list(input()))
combo = 0

while True:
	visited = [[False for x in range(6)] for y in range(12)]
	puyo = False
	for y in range(12):
		for x in range(6):
			if Map[y][x] != '.' and not visited[y][x]:
				Puyo(y, x, Map[y][x])
	if not puyo:
		break
	down()
	combo += 1

print(combo)