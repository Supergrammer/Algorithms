import sys
input = sys.stdin.readline

def DP(n):
	if n <= 1:
		return 0
	if memoi[n] != -1:
		return memoi[n]
	
	div3 = DP(n // 3) + n % 3 + 1
	div2 = DP(n // 2) + n % 2 + 1

	memoi[n] = min(div3, div2)
	return memoi[n]

N = int(input())
memoi = [-1] * 1000001
print(DP(N))