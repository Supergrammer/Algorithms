from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Map = []
visited = [[False for x in range(N)] for y in range(N)]

def find(lev: int):
	cnt = 0
	for y in range(N):
		for x in range(N):
			if Map[y][x] > lev - 1 and not visited[y][x]:
				BFS(y, x, lev)
				cnt += 1
	return cnt

def BFS(y, x, lev: int):
	Q = deque([[y, x]])
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

	while Q:
		y, x = Q.popleft()

		for dy, dx in dir:
			iy, ix = y + dy, x + dx
			if 0 <= iy < N and 0 <= ix < N and \
			   Map[iy][ix] > lev - 1 and not visited[iy][ix]:
				Q.append([iy, ix])
				visited[iy][ix] = True

def solution():
	safe = 1
	global visited

	for i in range(N):
		Map.append(list(map(int, input().split())))

	mx = max(list(map(max, Map)))
	mn = min(list(map(min, Map)))

	for i in range(mn, mx + 1):
		safe = max(safe, find(i))
		visited = [[False for x in range(N)] for y in range(N)]

	print(safe)

solution()