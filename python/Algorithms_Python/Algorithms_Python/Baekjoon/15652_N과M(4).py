import sys
input = sys.stdin.readline

def seq(seqarr):
	if len(seqarr) == M:
		print(' '.join(seqarr))
		return

	for i in map(str, range(int(seqarr[-1]) if seqarr else 1, N + 1)):
		seqarr += [i]
		seq(seqarr)
		seqarr.pop()

N, M = map(int, input().split())
seq([])