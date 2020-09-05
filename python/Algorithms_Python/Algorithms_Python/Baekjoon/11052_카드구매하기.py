import sys
input = sys.stdin.readline

N = int(input())
card = [0] + list(map(int, input().split()))
mem = [0] * (N + 1)

for i in range(1, N + 1):
	if mem[i] < card[i]:
		mem[i] = card[i]
	for j in range(i):
		if mem[i] < mem[j] + card[i - j]:
			mem[i] = mem[j] + card[i - j]

print(mem[N])