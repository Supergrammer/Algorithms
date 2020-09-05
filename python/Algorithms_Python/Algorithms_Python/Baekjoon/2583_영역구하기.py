from collections import deque
import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
Map = [[0 for x in range(N)] for y in range(M)]
visited = [[False for x in range(N)] for y in range(M)]
rst = []

def fill():
	for i in range(K):
		x1, y1, x2, y2 = map(int, input().split())
		for y in range(y1, y2):
			for x in range(x1, x2):
				Map[y][x] = 1

def BFS(y, x):
	Q = deque([[y, x]])
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	cnt = 1

	while Q:
		y, x = Q.popleft()
		for dy, dx in dir:
			iy, ix = y + dy, x + dx
			if 0 <= iy < M and 0 <= ix < N and \
			   Map[iy][ix] == 0 and not visited[iy][ix]:
				Q.append([iy, ix])
				visited[iy][ix] = True
				cnt += 1
	rst.append(cnt)

def solution():
	fill()
	for y in range(M):
		for x in range(N):
			if Map[y][x] == 0 and not visited[y][x]:
				visited[y][x] = True
				BFS(y, x)

	print(len(rst))
	for i in sorted(rst):
		print(i, end = ' ')

solution()