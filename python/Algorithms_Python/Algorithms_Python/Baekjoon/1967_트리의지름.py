import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
Map = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(N - 1):
	fr, to, leng = map(int, input().split())
	Map[fr].append((to, leng))
	Map[to].append((fr, leng))

def findFarthest(node, dist):
	visited[node] = True
	mem[node] = dist

	for n in Map[node]:
		if not visited[n[0]]:
			findFarthest(n[0], dist + n[1])

	visited[node] = False
	return

def nodeindex():
	node, dist = 0, 0
	for i in range(1, N + 1):
		if mem[i] > dist:
			node = i; dist = mem[i]
	return node, dist

mem = [0] * (N + 1)
findFarthest(1, 0)
node = nodeindex()[0]
mem = [0] * (N + 1)
findFarthest(node, 0)

print(nodeindex()[1])