import sys
input = sys.stdin.readline

T = int(input())

fibonacci = [0, 1, 1] + [0] * 38 + [1]
for i in range(2, 41):
	fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

for _ in range(T):
	N = int(input())
	print(fibonacci[N - 1], end=' ')
	print(fibonacci[N])