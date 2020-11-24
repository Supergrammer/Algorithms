#import sys
#input = sys.stdin.readline

#def SS_season():
#	for i in range(N):
#		for j in range(N):
#			for k in range(len(Map[i][j])):
#				if nutri[i][j] >= Map[i][j][k]:
#					nutri[i][j] -= Map[i][j][k]
#					Map[i][j][k] += 1
#				else:
#					nutri[i][j] += sum(Map[i][j][k:]) // 2
#					Map[i][j] = Map[i][j][:k]
#					break

#def FW_season():
#	for i in range(N):
#		for j in range(N):
#			for n in range(len(Map[i][j])):
#				if Map[i][j][n] % 5 == 0:
#					for k in range(-1, 2):
#						for l in range(-1, 2):
#							if k == 0 and l == 0:
#								continue
#							if 0 <= i + k < N and 0 <= j + l < N:
#								Map[i + k][j + l] = [1] + Map[i + k][j + l]
#			nutri[i][j] += A[i][j]


#N, M, K = map(int, input().split())
#nutri = [[5] * N for _ in range(N)]
#A = []
#Map = [[[] for _ in range(N)] for _ in range(N)]
#for _ in range(N):
#	A.append(list(map(int, input().split())))
#for _ in range(M):
#	x, y, z = map(int, input().split())
#	Map[x - 1][y - 1].append(z)

#for _ in range(K):
#	SS_season()
#	FW_season()

#sum = 0
#for i in range(N):
#	for j in range(N):
#		sum += len(Map[i][j])

#print(sum)

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
Food = [list(map(int, input().split())) for _ in range(N)]
nutri = [[5] * N for _ in range(N)]
Map = [[[] for _ in range(N)] for _ in range(N)]
dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for _ in range(M):
	x, y, z = map(int, input().split())
	Map[x - 1][y - 1].append(z)

def init():
	for i in range(N):
		for j in range(N):
			Map[i][j].sort()

def SS_Season():
	for i in range(N):
		for j in range(N):
			if Map[i][j]:
				dead = []
				for k in range(len(Map[i][j])):
					if Map[i][j][k] <= nutri[i][j]:
						nutri[i][j] -= Map[i][j][k]
						Map[i][j][k] += 1
					else:
						dead = Map[i][j][k:]
						Map[i][j] = Map[i][j][:k]
						break
				
				for k in dead:
					nutri[i][j] += k // 2

def FW_Season():
	for i in range(N):
		for j in range(N):
			if Map[i][j]:
				cnt = 0
				for k in range(len(Map[i][j])):
					if Map[i][j][k] % 5 == 0:
						cnt += 1

				if cnt:
					for dy, dx in dir:
						iy, ix = i + dy, j + dx
						if 0 <= iy < N and 0 <= ix < N:
							Map[iy][ix] = [1] * cnt + Map[iy][ix]
			nutri[i][j] += Food[i][j]

init()
for _ in range(K):
	SS_Season()
	FW_Season()

answer = 0
for i in range(N):
	for j in range(N):
		if Map[i][j]:
			answer += len(Map[i][j])

print(answer)