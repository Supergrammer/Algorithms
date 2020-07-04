from collections import deque
import sys
input = sys.stdin.readline

def BFS(n: int):
	Q = deque([n])
	visited = [-1 for i in range(N + 1)]
	visited[n] = 0
	time = 0
	global mn, rst

	while Q:
		time += 1
		size = len(Q)
		while size != 0:
			p = Q.popleft()
			size -= 1
			for i in Map[p]:
				if visited[i] == -1:
					Q.append(i)
					visited[i] = time
	if mn > sum(visited):
		mn = sum(visited)
		rst = n

if __name__ == '__main__':
	N, M = map(int, input().split())
	Map = [[] for i in range(N + 1)]
	mn = sys.maxsize
	rst = 0

	for i in range(M):
		fr, to = map(int, input().split())
		Map[fr].append(to)
		Map[to].append(fr)

	for i in range(N):
		BFS(i + 1)

	print(rst)