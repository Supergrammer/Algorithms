from collections import deque
import sys
input = sys.stdin.readline

def BFS(Q: []):
	visited = [[False for x in range(C)] for y in range(R)]
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	time = 0

	Q.append(S + ['S'])
	while Q:
		time += 1
		size = len(Q)
		while size != 0:
			y, x, c = Q.popleft()
			size -= 1
			for dy, dx in dir:
				iy, ix = y + dy, x + dx
				if [iy, ix] == D and c == 'S':
					return time
				if 0 <= iy < R and 0 <= ix < C and not visited[iy][ix]:
					if Map[iy][ix] in ['.', 'S']:
						Map[iy][ix] = c
						Q.append([iy, ix, c])
						visited[iy][ix] = True
	return 'KAKTUS'

if __name__ == "__main__":
	R, C = map(int, input().split())
	Map = []
	Q = deque([])

	for y in range(R):
		Map.append(list(input()))
		for x in range(C):
			if Map[y][x] == '*':
				Q.append([y, x, '*'])
			elif Map[y][x] == 'S':
				S = [y, x]
			elif Map[y][x] == 'D':
				D = [y, x]
	print(BFS(Q))