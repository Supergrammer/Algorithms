import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
Map = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
memoi = [[-1] * M for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

visited[0][0] = True

def check(y, x):
	if 0 <= y < N and 0 <= x < M:
		return True
	return False

def find(y, x):
	if memoi[y][x] != -1:
		return memoi[y][x]

	mx = 0

	for dy, dx in dir:
		iy, ix = y + dy * int(Map[y][x]), x + dx * int(Map[y][x])
		if check(iy, ix):
			if Map[iy][ix] == Map[y][x] or visited[iy][ix]:
				print(-1); sys.exit()
			elif Map[iy][ix] == 'H':
				continue
			else:
				visited[iy][ix] = True
				mx = max(mx, find(iy, ix))
				visited[iy][ix] = False

	if mx == 0: memoi[y][x] = 1
	else: memoi[y][x] = mx + 1
	
	return memoi[y][x]

print(find(0, 0))