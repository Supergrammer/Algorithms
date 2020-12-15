from collections import deque
import sys
input = sys.stdin.readline

prime = [True] * 10000
visited = [False] * 10000

prime[1] = False

for i in range(2, 101):
	if prime[i]:
		for j in range(i * 2, 10000):
			if prime[j] and j % i == 0:
				prime[j] = False

def find(A, B):
	if A == B:
		return 0

	Q = deque([A])
	time = 0
	visited[int(A)] = True

	while Q:
		size = len(Q)
		time += 1
		for _ in range(size):
			n = Q.popleft()
			for i in range(4):
				for j in range(10):
					dn = n[:i] + str(j) + n[i + 1:]
					if int(dn) < 1000 or not prime[int(dn)] or visited[int(dn)]:
						continue
					if dn == B:
						return time

					Q.append(dn)
					visited[int(dn)] = True
	return 'Impossible'

for _ in range(int(input())):
	A, B = input().split()
	print(find(B, A))