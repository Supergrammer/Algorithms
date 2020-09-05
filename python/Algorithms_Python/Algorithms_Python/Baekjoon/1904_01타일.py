import sys
input = sys.stdin.readline

N = int(input())

if N < 3:
	print(N)
else:
	mem1, mem2 = 2, 3
	for _ in range(N - 3):
		mem1, mem2 = mem2, (mem1 + mem2) % 15746
	print(mem2)