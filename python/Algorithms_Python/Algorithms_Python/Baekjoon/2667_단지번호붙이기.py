from collections import deque

def BFS(iy, ix):
	Q = deque([[iy, ix]])
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	size = 0

	while Q:
		y, x = Q.popleft()
		size += 1
		
		for dy, dx in dir:
			if 0 <= y + dy < N and 0 <= x + dx < N and \
				Map[y + dy][x + dx] == '1' and not visited[y + dy][x + dx]:
				Q.append([y + dy, x + dx])
				visited[y + dy][x + dx] = True
	
	cnt.append(size)

N = int(input())
Map = [] * N
visited = [[False for x in range(N)] for y in range(N)]
cnt = []

for i in range(N):
	Map.append(list(input()))

for y in range(N):
	for x in range(N):
		if Map[y][x] == '1' and not visited[y][x]:
			visited[y][x] = True
			BFS(y, x)

print(len(cnt))
for i in sorted(cnt):
	print(i)