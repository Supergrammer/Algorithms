import sys
input = sys.stdin.readline

def move(ipt: []):
	dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	ronum, command, repeat = int(ipt[0]), ipt[1], int(ipt[2])

	if command == 'L':
		robot[ronum][2] = (robot[ronum][2] - repeat) % 4
	elif command == 'R':
		robot[ronum][2] = (robot[ronum][2] + repeat) % 4
	else:
		for i in range(repeat):
			Map[robot[ronum][0]][robot[ronum][1]] = 0
			for j in range(2):
				robot[ronum][j] += dir[robot[ronum][2]][j]

			if 0 < robot[ronum][0] <= B and 0 < robot[ronum][1] <= A:
				if Map[robot[ronum][0]][robot[ronum][1]] == 0:
					Map[robot[ronum][0]][robot[ronum][1]] = ronum
				else:
					print("Robot {0} crashes into robot {1}"\
						.format(ronum, Map[robot[ronum][0]][robot[ronum][1]]))
					return False
			else:
				print("Robot {0} crashes into the wall".format(ronum))
				return False
	
	return True

A, B = map(int, input().split())
N, M = map(int, input().split())
Map = [[0] * (A + 1) for i in range(B + 1)]
robot, key = [[]], { 'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3 }

for i in range(N):
	ipt = list(map(str, input().split()))
	ipt[0], ipt[1], ipt[2] = int(ipt[1]), int(ipt[0]), key[ipt[2]]
	Map[ipt[0]][ipt[1]] = i + 1
	robot.append(ipt)

for i in range(M):
	if not move(list(map(str, input().split()))):
		break
	if i == M - 1:
		print("OK")