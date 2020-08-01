import sys
input = sys.stdin.readline

def territory():
	sum = 0

	for y in range(N):
		for x in range(M):
			if Map[y][x] == 1:
				for dy, dx in dir:
					iy, ix = y + dy, x + dx
					if 0 <= iy < N and 0 <= ix < M and Map[iy][ix] == 0:
						sum += 1
	return sum

inp = input().split(';')
Map = []
for row in inp:
	Map.append(list(map(int, row.split())))
N, M = len(Map), len(Map[0])
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

print(territory())