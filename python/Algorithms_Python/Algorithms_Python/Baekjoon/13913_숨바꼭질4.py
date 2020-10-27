from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001

visited[N] = 100001
answer = deque([])

def parent(n):
	while True:
		answer.appendleft(n)
		if visited[n] == 100001:
			break
		n = visited[n]

def find():
	if N == K: return 0

	Q = deque([N])
	time = 0

	while Q:
		size = len(Q)
		time += 1
		while size != 0:
			n = Q.popleft()
			size -= 1

			for dn in [n * 2, n - 1, n + 1]:
				if not (0 <= dn <= 100000 and visited[dn] == -1):
					continue
				
				visited[dn] = n
				Q.append(dn)
				if dn == K:
					return time

if N > K:
	print(N - K)
	for i in range(N, K - 1, -1):
		print(i, end=' ')
else:
	print(find())
	parent(K)
	for i in answer:
		print(i, end=' ')