from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map = []
visited = [[[False for b in range(2)] for x in range(M)] for y in range(N)]

def BFS():
	Q = deque([[0, 0, 0]])
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	tr = 1

	while Q:
		siz = len(Q)
		tr += 1
		while siz != 0:
			y, x, b = Q.popleft()
			siz -= 1
			for dy, dx in dir:
				iy, ix = y + dy, x + dx
				if [iy, ix] == [N - 1, M - 1]:
					return tr
				if 0 <= iy < N and 0 <= ix < M:
					if Map[iy][ix] == '0' and not visited[iy][ix][b]:
						Q.append([iy, ix, b])
						visited[iy][ix][b] = True
					elif Map[iy][ix] == '1' and b == 0 and not visited[iy][ix][b + 1]:
						Q.append([iy, ix, b + 1])
						visited[iy][ix][b + 1] = True
	return -1

def solution():
	if N == M == 1:
		print(1)
		return
	for i in range(N):
		Map.extend(input().split())
	print(BFS())

solution()