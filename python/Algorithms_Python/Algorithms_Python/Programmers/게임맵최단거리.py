from collections import deque

def solution(maps):
	answer = 1
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

	n, m = len(maps), len(maps[0])
	visited = [[False] * m for _ in range(n)]

	Q = deque([[0, 0]])

	while Q:
		size = len(Q)
		answer += 1

		for _ in range(size):
			y, x = Q.popleft()
			for dy, dx in dir:
				iy, ix = y + dy, x + dx

				if iy == n - 1 and ix == m - 1: return answer
				if 0 <= iy < n and 0 <= ix < m and\
					not visited[iy][ix] and maps[iy][ix] == 1:
					Q.append([iy, ix])
					visited[iy][ix] = True

	return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))