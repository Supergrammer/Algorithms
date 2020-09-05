from collections import deque
import sys
input = sys.stdin.readline

def BFS():
	tr = -1
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	while Q:
		tr += 1
		siz = len(Q)
		
		while siz != 0:
			y, x = Q.popleft()
			siz -= 1

			for dy, dx in dir:
				iy, ix = y + dy, x + dx
				if 0 <= iy < N and 0 <= ix < M and \
					Map[iy][ix] == 0 and not visited[iy][ix]:
					Q.append([iy, ix])
					Map[iy][ix] = 1
					visited[iy][ix] = True

	for y in range(N):
		for x in range(M):
			if Map[y][x] == 0:
				return -1
	return tr

M, N = map(int, input().split())
Map = []
visited = [[False for x in range(M)] for y in range(N)]
Q = deque([])

for i in range(N):
	Map.append(list(map(int, input().split())))

for y in range(N):
	for x in range(M):
		if Map[y][x] == 1:
			Q.append([y, x])

print(BFS())