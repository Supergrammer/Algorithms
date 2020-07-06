from collections import deque
import sys
input = sys.stdin.readline

def BFS():
	if S == G:
		return 0

	Q = deque([S])
	visited[S] = True
	time = 0

	while Q:
		time += 1
		size = len(Q)
		while size != 0:
			n = Q.popleft()
			size -= 1
			for i in [n + U, n - D]:
				if i == G:
					return time
				if 1 <= i <= F and not visited[i]:
					Q.append(i)
					visited[i] = True
	return 'use the stairs'

F, S, G, U, D = map(int, input().split())
visited = [False for i in range(F + 1)]

print(BFS())