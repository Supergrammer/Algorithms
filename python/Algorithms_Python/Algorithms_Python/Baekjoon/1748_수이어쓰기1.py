import sys
input = sys.stdin.readline

N = input().strip()
sum = 0

for i in range(len(N) - 1):
	sum += (10 ** i * 9 * (i + 1))
sum += (int(N) - (10 ** (len(N) - 1)) + 1) * len(N)

print(sum)