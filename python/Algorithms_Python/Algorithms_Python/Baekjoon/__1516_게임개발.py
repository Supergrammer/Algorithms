from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cost = [0] * (N + 1)
pre = [[] for _ in range(N + 1)]
graph = [[False] * (N + 1) for _ in range(N + 1)]

Q = deque([])
for i in range(1, N + 1):
	tmp = list(map(int, input().split()))
	cost[i] = tmp[0]

	if not tmp[1:-1]: Q.append(i)
	graph[i] = tmp[1:-1]
	for j in tmp[1:-1]:
		pre[j].append(i)

def topology():
	pass

print(1)