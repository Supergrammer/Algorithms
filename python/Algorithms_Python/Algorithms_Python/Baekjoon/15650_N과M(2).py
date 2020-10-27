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
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for seq in combinations(list(map(str, range(1, N + 1))), M):
	print(' '.join(seq))
"""