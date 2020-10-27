from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for seq in permutations(list(map(str, sorted(map(int, input().split())))), M):
	print(' '.join(seq))