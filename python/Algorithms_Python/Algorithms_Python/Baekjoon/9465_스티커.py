import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N = int(input())
	sticker = []
	for i in range(2):
		sticker.append(list(map(int, input().split())))

	if N == 1:
		print(max(sticker))
	else:
		mem = [[0] * N, [0] * N]
		mem[0][0], mem[0][1], mem[1][0], mem[1][1] = \
			sticker[0][0], sticker[0][1] + sticker[1][0], sticker[1][0], sticker[0][0] + sticker[1][1]

		for i in range(2, N):
			mem[0][i] = max(mem[1][i - 1], mem[1][i - 2]) + sticker[0][i]
			mem[1][i] = max(mem[0][i - 1], mem[0][i - 2]) + sticker[1][i]

		print(max(mem[0][N - 1], mem[1][N - 1]))