import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (M + 1)]

for _ in range(N):
	arr.append([0] + list(map(int, input().split())))

for i in range(1, N + 1):
	for j in range(1, M + 1):
		arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

K = int(input())
for _ in range(K):
	i, j, k, l = map(int, input().split())
	sum = arr[k][l] - arr[i - 1][l] - arr[k][j - 1] + arr[i - 1][j - 1]
	print(sum)