import sys
input = sys.stdin.readline

N = int(input())
mem = [0] * (N)

try:
	mem[0] = mem[1] = 1
	for i in range(2, N):
		mem[i] = mem[i - 1] + mem[i - 2]
	print(mem[N - 1])

except:
	print(1)