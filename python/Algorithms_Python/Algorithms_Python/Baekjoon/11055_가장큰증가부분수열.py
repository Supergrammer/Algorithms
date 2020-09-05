import sys
input = sys.stdin.readline

A = int(input())
seq = list(map(int, input().split()))
mem = [0] * A

for i in range(A):
	mem[i] = seq[i]
	for j in range(i):
		if seq[j] < seq[i]:
			mem[i] = max(mem[i], seq[i] + mem[j])

print(max(mem))