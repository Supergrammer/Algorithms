from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
fr, to = map(int, input().split())
M = int(input())
Map = [[] for i in range(N + 1)]

def BFS():
	Q = deque([fr])
	visited = [False for i in range(N + 1)]
	visited[fr] = True
	tr = 0
	while Q:
		tr += 1
		siz = len(Q)
		while siz != 0:
			n = Q.popleft()
			siz -= 1
			for i in Map[n]:
				if i == to:
					return tr
				if not visited[i]:
					Q.append(i)
					visited[i] = True
	return -1

if __name__ == "__main__":
	for i in range(M):
		parent, child = map(int, input().split())
		Map[parent].append(child)
		Map[child].append(parent)
	print(BFS())