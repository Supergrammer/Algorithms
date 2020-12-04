from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]

def init():
	for i in range(N):
		for j in range(N):
			if Map[i][j] == 9:
				Map[i][j] = 0
				return [i, j]

def check(y, x):
	if 0 <= y < N and 0 <= x < N:
		return True
	return False

def find():
	Q = deque([now])
	time = 0

	visited = [[False] * N for _ in range(N)]
	visited[now[0]][now[1]] = True
	canMove = []

	while Q:
		size = len(Q)
		time += 1

		for _ in range(size):
			y, x = Q.popleft()
			for dy, dx in dir:
				iy, ix = y + dy, x + dx
				if check(iy, ix) and not visited[iy][ix]:
					visited[iy][ix] = True
					if shark >= Map[iy][ix]:
						if Map[iy][ix] != 0 and Map[iy][ix] != shark:
							canMove.append([iy, ix])
						else:
							Q.append([iy, ix])
		if canMove: break

	if canMove:
		canMove = sorted(canMove, key=lambda x:(x[0], x[1]))
		return time, [canMove[0][0], canMove[0][1]]
	else:
		return -1, []
		
now = init()
shark, count = 2, 0
answer = 0

while True:
	time, now = find()

	if time == -1:
		break
	else:
		answer += time
		count += 1
		if shark == count:
			shark += 1; count = 0
		Map[now[0]][now[1]] = 0

print(answer)