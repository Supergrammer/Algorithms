from collections import deque
import sys
input = sys.stdin.readline

def BFS(fr, to, I):
	if fr == to:
		return 0

	Q = deque([fr])
	tr = 0
	dir = [[-1, -2], [-2, -1], [-2, 1], [-1, 2],
		[1, 2], [2, 1], [2, -1], [1, -2]]
	visited = [[False for x in range(I)] for y in range(I)]
	visited[fr[0]][fr[1]] = True

	while Q:
		tr += 1
		siz = len(Q)

		while siz != 0:
			y, x = Q.popleft()
			siz -= 1
			for dy, dx in dir:
				iy, ix = y + dy, x + dx
				if [iy, ix] == to:
					return tr
				if 0 <= iy < I and 0 <= ix < I and not visited[iy][ix]:
					Q.append([iy, ix])
					visited[iy][ix] = True
	return tr

def solution():
	T = int(input())
	for i in range(T):
		I = int(input())
		fr = list(map(int, input().split()))
		to = list(map(int, input().split()))

		print(BFS(fr, to, I))

solution()