import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(str, sorted(map(int, input().split()))))

def seq(seqarr, idx):
	if len(seqarr) == M:
		print(' '.join(seqarr))
		return

	for i in range(idx, N):
		seqarr += [arr[i]]
		seq(seqarr, i)
		seqarr.pop()

seq([], 0)