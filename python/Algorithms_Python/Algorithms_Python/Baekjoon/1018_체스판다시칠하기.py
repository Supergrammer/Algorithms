import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map = []
rst = 10 ** 4

for _ in range(N):
	Map.append(list(input()))

for i in range(N - 7):
	for j in range(M - 7):
		cnt = 0
		for y in range(8):
			for x in range(8):
				if (x + y) % 2 == 0 and Map[i + y][j + x] == 'W':
					cnt += 1
				elif (x + y) % 2 == 1 and Map[i + y][j + x] == 'B':
					cnt += 1
		cnt = min(cnt, 64 - cnt)
		rst = min(rst, cnt)

print(rst)