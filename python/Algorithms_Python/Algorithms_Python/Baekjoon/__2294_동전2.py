import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
inf = 10000

def DP(n):
	if mem[n] != -1: return mem[n]

	mn = inf
	for i in rem:
		if n - i <= 0: continue
		mn = min(mn, DP(n - i))

	if mn != -1 and mn != inf:
		mem[n] = mn + 1
	
	return mem[n]

N, K = map(int, input().split())
mem = [-1] * (K + 1)

arr = [0] + sorted([int(input()) for _ in range(N)])
mem[ipt] = 1
rem.append(ipt)

print(DP(K))