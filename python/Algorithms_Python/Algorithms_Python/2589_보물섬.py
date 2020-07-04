from collections import deque
import sys
input = sys.stdin.readline

def BFS(y, x):
	Q = deque([[y, x]])
	visited = [[False for x in range(W)] for y in range(H)]
	visited[y][x] = True
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	time = -1
	while Q:
		time += 1
		size = len(Q)
		while size != 0:
			y, x = Q.popleft()
			size -= 1
			for dy, dx in dir:
				iy, ix = y + dy, x + dx
				if 0 <= iy < H and 0 <= ix < W and \
					Map[iy][ix] == 'L' and not visited[iy][ix]:
					Q.append([iy, ix])
					visited[iy][ix] = True
	return time

H, W = map(int, input().split())
Map = []
mx = 0

for i in range(H):
	Map.append(list(input()))

for y in range(H):
	for x in range(W):
		if Map[y][x] == 'L':
			mx = max(mx, BFS(y, x))
print(mx)