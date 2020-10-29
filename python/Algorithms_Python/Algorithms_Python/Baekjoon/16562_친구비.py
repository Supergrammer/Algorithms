import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
friendcost = [0] + list(map(int, input().split()))
group = [i for i in range(N + 1)]
answer = 0

def union(a, b):
	a, b = find(a), find(b)
	if a == b:
		return

	if a > b:
		a, b = b, a

	friendcost[a] = min(friendcost[a], friendcost[b])
	group[b] = a

def find(n):
	if n == group[n]:
		return n

	group[n] = find(group[n])
	return group[n]

for _ in range(M):
	v, w = map(int, input().split())
	union(v, w)

for i in range(1, N + 1):
	if find(i) == i:
		answer += friendcost[i]
	if answer > K:
		break

print(answer if answer <= K else "Oh no")

"""
from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
friendcost = [0] + list(map(int, input().split()))
relation = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(M):
	v, w = map(int, input().split())
	relation[v].append(w)
	relation[w].append(v)

def find(n):
	Q = deque([n])
	mn = friendcost[n]
	visited[n] = True

	while Q:
		n = Q.popleft()
		for dn in relation[n]:
			if not visited[dn]:
				Q.append(dn)
				visited[dn] = True
				mn = min(mn, friendcost[dn])

	return mn

for i in range(1, N + 1):
	if not visited[i]:
		answer += find(i)
	if answer > K: break

print(answer if answer <= K else "Oh no")
"""