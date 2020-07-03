from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Map = []
visited = [[False for x in range(N)] for y in range(N)]

def area():
	cnt = 0
	for y in range(N):
		for x in range(N):
			if not visited[y][x]:
				BFS(y, x, Map[y][x])
				cnt += 1
	return cnt

def BFS(y, x, c: str):
	Q = deque([[y, x]])
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	
	while Q:
		y, x = Q.popleft()
		for dy, dx in dir:
			iy, ix = y + dy, x + dx
			if 0 <= iy < N and 0 <= ix < N and \
				Map[iy][ix] == c and not visited[iy][ix]:
				Q.append([iy, ix])
				visited[iy][ix] = True

def colorweakness():
	for y in range(N):
		for x in range(N):
			visited[y][x] = False
			if Map[y][x] == 'R':
				Map[y][x] = 'G'

def solution():
	for i in range(N):
		Map.append(list(input()))
	
	normal = area()
	colorweakness()
	coweek = area()
	
	return normal, coweek

for i in solution():
	print(i, end = ' ')