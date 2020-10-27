from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for seq in permutations(list(map(str, range(1, N + 1))), M):
	print(' '.join(seq))

"""
import sys
input = sys.stdin.readline

def seq(seqarr):
	if len(seqarr) == M:
		for i in seqarr:
			print(i, end=' ')
		print()

	for i in range(1, N + 1):
		if not visited[i]:
			seqarr += [i]; visited[i] = True 
			seq(seqarr)
			seqarr.pop(); visited[i] = False

N, M = map(int, input().split())
visited = [False] * (N + 1)
seq([])
"""

"""
import sys
input = sys.stdin.readline

def seq(seqarr):
	if len(seqarr) == M:
		for i in seqarr:
			print(i, end=' ')
		print()

	start = 1
	if seqarr:
		start = seqarr[-1] + 1
	for i in range(start, N + 1):
		seqarr += [i]
		seq(seqarr)
		seqarr.pop()

N, M = map(int, input().split())
seq([])
"""