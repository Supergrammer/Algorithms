from collections import deque
import sys
input = sys.stdin.readline


def year():
	tmp = [[0 for x in range(M)] for y in range(N)]
	for y in range(N):
		for x in range(M):
			if Map[y][x] != 0:
				for dy, dx in dir:
					iy, ix = y + dy, x + dx
					if 0 <= iy < N and 0 <= ix < M and Map[iy][ix] == 0:
						tmp[y][x] -= 1
#	for y in range(N):
#		Map[y] = [a + b for a, b in zip(Map[y], tmp[y])]
	for y in range(N):
		for x in range(M):
			Map[y][x] += tmp[y][x]
			if Map[y][x] < 0: Map[y][x] = 0
		
def calcarea():
	Q = deque([])
	visited = [[False for x in range(M)] for y in range(N)]
	area = 0
	for y in range(N):
		for x in range(M):
			if Map[y][x] != 0 and not visited[y][x]:
				Q.append([y, x])
				visited[y][x] = True

				while Q:
					qy, qx = Q.popleft()
					for dy, dx in dir:
						iy, ix = qy + dy, qx + dx
						if 0 <= iy < N and 0 <= ix < M and \
						   not visited[iy][ix] and Map[iy][ix] != 0:
							Q.append([iy, ix])
							visited[iy][ix] = True
				area += 1
	return area

N, M = map(int, input().split())
Map = []
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
time = 0
for i in range(N):
	Map.append(list(map(int, input().split())))

while True:
	rst = calcarea()

	if rst > 1:
		print(time); break
	elif rst == 0:
		print(0); break

	year()
	time += 1