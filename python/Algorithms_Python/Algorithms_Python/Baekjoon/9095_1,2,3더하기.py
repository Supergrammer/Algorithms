import sys
input = sys.stdin.readline

def DP(n):
	if mem[n] != -1:
		return mem[n]

	mem[n] = DP(n - 1) + DP(n - 2) + DP(n - 3)
	return mem[n]

T = int(input())
for _ in range(T):
	N = int(input())
	mem = [-1, 1, 2, 4] + [-1 for i in range(N - 3)]
	print(DP(N))