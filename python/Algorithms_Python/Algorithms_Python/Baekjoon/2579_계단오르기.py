import sys
input = sys.stdin.readline

N = int(input())
stairs = [-1] * N
mem = [-1] * N

for i in range(N):
	stairs[i] = int(input())

try:
	mem[0], mem[1], mem[2] = \
		stairs[0], stairs[0] + stairs[1], max(stairs[0], stairs[1]) + stairs[2]
	for i in range(3, N):
		mem[i] = max(mem[i - 3] + stairs[i - 1], mem[i - 2]) + stairs[i]
	
	print(mem[-1])

except:
	print(sum(stairs))