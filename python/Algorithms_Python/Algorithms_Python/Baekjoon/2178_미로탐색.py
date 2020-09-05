from collections import deque

def BFS():
	Q = deque([[0, 0]])
	tr, size = 1, 0
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	
	while Q:
		tr += 1
		size = len(Q)

		while size != 0:
			y, x = Q.popleft()
			size -= 1

			for dy, dx in dir:
				if 0 <= y + dy < N and 0 <= x + dx < M and not visited[y + dy][x + dx] and Map[y + dy][x + dx] == '1':
					if y + dy == N - 1 and x + dx == M - 1:
						return tr
					Q.append([y + dy, x + dx])
					visited[y + dy][x + dx] = True

N, M = map(int, input().split())
Map = [] * N
visited = [[False for x in range(M)] for y in range(N)]

for i in range(N):
	Map.append(list(input()))

print(BFS())