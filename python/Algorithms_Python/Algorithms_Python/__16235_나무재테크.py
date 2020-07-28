import sys
input = sys.stdin.readline

def SS_season():
	for i in range(N):
		for j in range(N):
			for k in range(len(Map[i][j])):
				if nutri[i][j] >= Map[i][j][k]:
					nutri[i][j] -= Map[i][j][k]
					Map[i][j][k] += 1
				else:
					nutri[i][j] += sum(Map[i][j][k:]) // 2
					Map[i][j] = Map[i][j][:k]
					break

def FW_season():
	for i in range(N):
		for j in range(N):
			for n in range(len(Map[i][j])):
				if Map[i][j][n] % 5 == 0:
					for k in range(-1, 2):
						for l in range(-1, 2):
							if k == 0 and l == 0:
								continue
							if 0 <= i + k < N and 0 <= j + l < N:
								Map[i + k][j + l] = [1] + Map[i + k][j + l]
			nutri[i][j] += A[i][j]


N, M, K = map(int, input().split())
nutri = [[5] * N for _ in range(N)]
A = []
Map = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(N):
	A.append(list(map(int, input().split())))
for _ in range(M):
	x, y, z = map(int, input().split())
	Map[x - 1][y - 1].append(z)

for _ in range(K):
	SS_season()
	FW_season()

sum = 0
for i in range(N):
	for j in range(N):
		sum += len(Map[i][j])

print(sum)