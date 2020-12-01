import sys
input = sys.stdin.readline

N = int(input())
Map = [list(input().strip()) for _ in range(N)]
dir = [[0, 0], [0, 1], [1, 0], [1, 1]]

def QuadTree(y, x, N):
	if N == 1:
		return Map[y][x]

	rtn = ''
	cnt = [0, 0]

	for dy, dx in dir:
		comp = QuadTree(y + dy * N // 2, x + dx * N // 2, N // 2)
		rtn += comp

		if comp[0] != '(':
			cnt[int(comp)] += 1

	if cnt[0] == 4: return '0'
	elif cnt[1] == 4: return '1'
	else: return '(' + rtn + ')'

print(QuadTree(0, 0, N))