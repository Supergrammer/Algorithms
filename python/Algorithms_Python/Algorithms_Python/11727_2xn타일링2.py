import sys
input = sys.stdin.readline

N = int(input())

if N in [1, 2]:
	print(N * 2 - 1)

else:
	mem = [0] * (N + 1)
	mem[1], mem[2] = 1, 3

	for i in range(3, N + 1):
		mem[i] = mem[i - 1] + mem[i - 2] * 2

	print(mem[N] % 10007)