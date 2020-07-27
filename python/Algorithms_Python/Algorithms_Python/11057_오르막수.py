import sys
input = sys.stdin.readline

N = int(input())
asc = [1 for _ in range(10)]

for _ in range(N - 1):
	for i in range(1, 10):
		asc[i] += asc[i - 1]

print(sum(asc) % 10007)