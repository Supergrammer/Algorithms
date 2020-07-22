import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
mem = [1] * (N)

for i in range(N):
	for j in range(i):
		if A[j] < A[i] and mem[i] < mem[j] + 1:
			mem[i] = mem[j] + 1

print(max(mem))