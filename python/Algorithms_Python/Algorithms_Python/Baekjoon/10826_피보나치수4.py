import sys
input = sys.stdin.readline

N = int(input())
def fibo(n):
	if n < 2: return n

	prv, nxt = 0, 1
	n -= 1
	while n:
		n -= 1
		prv, nxt = nxt, prv + nxt

	return nxt

print(fibo(N))