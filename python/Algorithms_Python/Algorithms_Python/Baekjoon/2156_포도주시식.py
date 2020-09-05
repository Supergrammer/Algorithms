import sys
input = sys.stdin.readline

N = int(input())
wine = [] + [0]
mem = [0] * (N + 1)

for _ in range(N):
	wine.append(int(input()))

try:
	mem[0], mem[1], mem[2] = \
		wine[0], wine[0] + wine[1], wine[2] + max(wine[0], wine[1])

	for i in range(3, N + 1):
		mem[i] = max(mem[i - 1], wine[i] + max(wine[i - 1] + mem[i - 3], mem[i - 2]))

	print(max(mem[N], mem[N - 1]))

except:
	print(sum(wine))