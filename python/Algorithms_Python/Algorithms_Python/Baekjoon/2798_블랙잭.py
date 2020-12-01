from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for comb in combinations(arr, 3):
	tmp = sum(comb)
	if answer < tmp <= M:
		answer = tmp
	if tmp == M: break

print(answer)