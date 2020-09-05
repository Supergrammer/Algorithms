from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

def link():
	for i in range(M):
		fr, to = map(int, input().split())
		Map[fr].append(to)
		Map[to].append(fr)

def BFS():
	cnt = 0
	for i in range(1, N + 1):
		if not visited[i]:
			Q = deque([i])
			visited[i] = True

			while Q:
				p = Q.popleft()

				for j in Map[p]:
					if not visited[j]:
						Q.append(j)
						visited[j] = True
			cnt += 1
	return cnt

def solution():
	link()
	print(BFS())

solution()