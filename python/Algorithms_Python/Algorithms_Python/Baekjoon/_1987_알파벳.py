import sys
input = sys.stdin.readline

def find(y, x, depth):
	global mx
	if mx < depth: mx = depth
	if mx == 26: return

	for dy, dx in dir:
		iy, ix = y + dy, x + dx
		if 0 <= iy < R and 0 <= ix < C:
			asc = ord(Map[iy][ix]) - ord('A')
			if not visited[asc]:
				visited[asc] = True
				find(iy, ix, depth + 1)
				visited[asc] = False

R, C = map(int, input().split())
Map = []
visited = [False for _ in range(26)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
mx = 0

for _ in range(R):
	Map.append(list(input().strip()))

visited[ord(Map[0][0]) - ord('A')] = True
find(0, 0, 1)

print(mx)