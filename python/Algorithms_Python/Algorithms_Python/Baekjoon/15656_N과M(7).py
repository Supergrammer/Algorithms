import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(str, sorted(map(int, input().split()))))

def seq(seqarr):
	if len(seqarr) == M:
		print(' '.join(seqarr))
		return

	for i in arr:
		seqarr += [i]
		seq(seqarr)
		seqarr.pop()

seq([])