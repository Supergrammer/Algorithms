import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N = int(input())
	mem = [1, 1, 1, 2, 2] + [0] * (N - 5)

	for i in range(5, N):
		mem[i] = mem[i - 1] + mem[i - 5]

	print(mem[N - 1])