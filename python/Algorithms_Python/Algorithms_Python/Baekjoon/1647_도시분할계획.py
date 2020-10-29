import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = sorted([list(map(int, input().split())) for _ in range(E)]\
	, key=lambda x:x[2])
parent = [i for i in range(V + 1)]
answer = 0

def union(a, b):
	a, b = find(a), find(b)
	if a > b:
		a, b = b, a

	parent[b] = find(a)

def find(n):
	if parent[n] == n:
		return n

	parent[n] = find(parent[n])
	return parent[n]

cnt = V - 2
for edge in graph:
	v1, v2, length = edge
	if find(v1) == find(v2):
		continue

	cnt -= 1
	union(v1, v2)
	answer += length

	if cnt == 0:
		break

print(answer)