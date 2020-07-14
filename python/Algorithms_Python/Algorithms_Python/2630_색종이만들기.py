import sys
input = sys.stdin.readline

def divide(y, x, length):
	w, b = 0, 0
	half = length // 2
	checked = check(y, x, length)
	if checked in ['w', 'b']:
		if checked == 'w': w += 1
		else: b += 1
		return w, b
	else:
		arr = [divide(y, x, half), divide(y + half, x, half),
		 divide(y, x + half, half), divide(y + half, x + half, half)]
		for arrw, arrb in arr:
			w += arrw; b += arrb
		return w, b

def check(sy, sx, length):
	w, b = 0, 0
	for y in range(sy, sy + length):
		for x in range(sx, sx + length):
			if Map[y][x] == 0: w += 1
			else: b += 1
	if w == 0: return 'b'
	elif b == 0: return 'w'
	else: return 'n'

N = int(input())
Map = []

for _ in range(N):
	Map.append(list(map(int, input().split())))

for i in divide(0, 0, N):
	print(i)