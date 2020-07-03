from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Map = []

def BFS(visited: [], Q: []):
	while Q:
		n = Q.popleft()

		for i in range(N):
			if Map[n][i] == 1 and visited[i] == 0:
				Q.append(i)
				visited[i] = 1

def solution():
	rst = []
	for i in range(N):
		Map.append(list(map(int, input().split())))

	for y in Map:
		visited = [0 for i in range(N)]
		Q = deque([])
		for x in range(N):
			if y[x] == 1:
				Q.append(x)
				visited[x] = 1
		BFS(visited, Q)
		rst.append(visited)

	for y in rst:
		for x in y:
			print(x, end = ' ')
		print()

solution()