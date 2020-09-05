import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N, M = map(int, input().split())

	for i in range(M - 1, M - N, -1):
		M *= i
	for i in range(N - 1, 0, -1):
		N *= i

	print(M // N)