from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for seq in combinations(list(map(str, sorted(map(int, input().split())))), M):
	print(' '.join(seq))