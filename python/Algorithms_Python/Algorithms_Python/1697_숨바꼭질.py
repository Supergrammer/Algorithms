from collections import deque
import sys
input = sys.stdin.readline

def BFS():
	if N == K:
		return 0

	Q = deque([N])
	visited[N] = True
	tr = 0

	while Q:
		tr += 1
		siz = len(Q)
		while siz != 0:
			n = Q.popleft()
			siz -= 1

			for mov in [n - 1, n + 1, n * 2]:
				if mov == K:
					return tr
				if 0 <= mov <= 100000 and not visited[mov]:
					Q.append(mov)
					visited[mov] = True

N, K = map(int, input().split())
visited = [False for i in range(100001)]

print(BFS())