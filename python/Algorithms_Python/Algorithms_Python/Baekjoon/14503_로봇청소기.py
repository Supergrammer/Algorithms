import sys
input = sys.stdin.readline

def init():
	for _ in range(N):
		Map.append(list(map(int, input().split())))

def loop():
	global r, c, d, clean
	if Map[r][c] == 0:
		Map[r][c] = 2
		clean += 1

	for i in range(1, 5):
		id = (d - i + 4) % 4
		dy, dx = dir[id]

		if Map[r + dy][c + dx] == 0:
			r += dy; c += dx; d = id
			return True

	dy, dx = dir[(d + 2) % 4]
	if Map[r + dy][c + dx] == 1:
		return False
	else:
		r += dy; c += dx
		return True

N, M = map(int, input().split())
r, c, d = map(int, input().split())
Map = []
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
clean = 0

init()
while loop():
	pass
print(clean)