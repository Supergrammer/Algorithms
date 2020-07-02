from collections import deque
import sys
input = sys.stdin.readline

def BFS(y, x):
	Q = deque([[y, x]])
	dir = [[-1, 0],[1,0],[0,-1],[0,1]]

	while Q:
		y, x = Q.popleft()

		for dy, dx in dir:
			iy, ix = y + dy, x + dx
			if 0 <= iy < N and 0 <= ix < M and \
				Map[iy][ix] == 1 and not visited[iy][ix]:
				Q.append([iy, ix])
				visited[iy][ix] = True

T = int(input())
for i in range(T):
	M, N, K = map(int, input().split())
	Map = [[0 for x in range(M)] for y in range(N)]
	visited = [[False for x in range(M)] for y in range(N)]
	cnt = 0

	for j in range(K):
		X, Y = map(int, input().split())
		Map[Y][X] = 1

	for y in range(N):
		for x in range(M):
			if Map[y][x] == 1 and not visited[y][x]:
				BFS(y, x)
				cnt+= 1
	print(cnt)