from collections import deque
import sys
input = sys.stdin.readline

def calcarea(y, x, ar):
	Q = deque([[y, x]])
	Map[y][x] = ar

	while Q:
		y, x = Q.popleft()
		for dy, dx in dir:
			iy, ix = y + dy, x + dx
			if check(iy, ix) and Map[iy][ix] == 1:
				Map[iy][ix] = ar
				Q.append([iy, ix])

def bridge():
	mn = sys.maxsize

	for y in range(N):
		for x in range(N):
			if Map[y][x] != 0:
				mn = min(mn, BFS(y, x, Map[y][x]))							
	return mn

def BFS(y, x, tmp):
	Q = deque([[y, x]])
	visited = [[False for x in range(N)] for y in range(N)]
	visited[y][x] = True
	time = 0

	while Q:
		time += 1
		size = len(Q)
		while size != 0:
			y, x = Q.popleft()
			size -= 1
			for dy, dx in dir:
				iy, ix = y + dy, x + dx
				if check(iy, ix) and not visited[iy][ix]:
					if Map[iy][ix] == 0:
						Q.append([iy, ix])
						visited[iy][ix] = True
					elif Map[iy][ix] != tmp:
						return time - 1
	return sys.maxsize

def check(y, x):
	if 0 <= y < N and 0 <= x < N:
		return True
	return False

N = int(input())
Map = []
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(N):
	Map.append(list(map(int, input().split())))

ar = 1
for y in range(N):
	for x in range(N):
		if Map[y][x] == 1:
			ar += 1
			calcarea(y, x, ar)

print(bridge())