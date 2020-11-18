def solution(m, n, puddles):
	answer = 0
	m += 1; n += 1

	Map = [[0] * (m) for _ in range(n)]
	Map[1][1] = 1

	for x, y in puddles:
		Map[y][x] = -1

	for i in range(1, n):
		for j in range(1, m):
			if Map[i][j] != -1:
				if Map[i - 1][j] != -1:
					Map[i][j] += Map[i - 1][j]
				if Map[i][j - 1] != -1:
					Map[i][j] += Map[i][j - 1]
				Map[i][j] %= 1000000007

	answer = Map[n - 1][m - 1]
	return answer

print(solution(4, 3, [[2, 2]]))