import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mem = [0] * (M + 1)

for i in range(1, N + 1):
	arr = [0] + list(map(int, input().split()))
	for j in range(1, M + 1):
		arr[j] += max(arr[j - 1], mem[j])
	mem = arr

print(mem[M])