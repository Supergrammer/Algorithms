from collections import deque

N, M, V = map(int, input().split())
grp = {}
visited = []

def BFS(node):
	Q = deque([node])

	while Q:
		n = Q.popleft()
		if n not in visited:
			visited.append(n)
			try: Q += sorted(grp[n] - set(visited))
			except KeyError: pass

def DFS(node):
	if node not in visited:
		visited.append(node)
		try:
			for n in sorted(grp[node]):
				DFS(n)
		except KeyError: pass

for i in range(M):
	fr, to = map(int, input().split())
	try: grp[fr].add(to)
	except KeyError: grp[fr] = {to}
	try: grp[to].add(fr)
	except KeyError: grp[to] = {fr}

DFS(V)
for i in visited:
	print(i, end=" ")
print()
visited = []
BFS(V)
for i in visited:
	print(i, end=" ")