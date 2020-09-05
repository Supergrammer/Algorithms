from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
Map = [[[] for y in range(N)] for z in range(H)]
visited = [[[False for x in range(M)] for y in range(N)] for z in range(H)]
Q = deque([])

def ipt():
	for z in range(H):
		for y in range(N):
			Map[z][y].extend(list(map(int, input().split())))
			for x in range(M):
				if Map[z][y][x] == 1:
					Q.append([z, y, x])
					visited[z][y][x] = True

def check():
	for z in range(H):
		for y in range(N):
			for x in range(M):
				if Map[z][y][x] == 0:
					return False
	return True

def BFS():
	tr = -1
	dir = [[-1, 0, 0], [1, 0, 0], [0, -1, 0],
		[0, 1, 0], [0, 0, -1], [0, 0, 1]]
	while Q:
		siz = len(Q)
		tr += 1
		while siz != 0:
			z, y, x = Q.popleft()
			siz -= 1
			for dz, dy, dx in dir:
				iz, iy, ix = z + dz, y + dy, x + dx
				if 0 <= iz < H and 0 <= iy < N and 0 <= ix < M and \
					Map[iz][iy][ix] == 0 and not visited[iz][iy][ix]:
					Map[iz][iy][ix] = 1
					Q.append([iz, iy, ix])
					visited[iz][iy][ix] = True
	return tr if check() else -1

def solution():
	ipt()
	print(BFS())

solution()