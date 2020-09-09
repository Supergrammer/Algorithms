def solution(m, n, board):
	answer = 0
	isDone = False

	for i in range(m):
		board[i] = list(board[i])

	while not isDone:
		isDone = True
		checked = [[0] * n for i in range(m)]
		for i in range(m - 1):			
			for j in range(n - 1):
				c = board[i][j]
				if c == '0': continue
				if board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] == c:
					checked[i][j] = checked[i + 1][j] = checked[i][j + 1] = checked[i + 1][j + 1] = '1'
					isDone = False

		for i in range(m):
			for j in range(n):
				if checked[i][j] == '1':
					board[i][j] = '0'
					answer += 1

		for i in range(n):
			tmp = []
			for j in range(m):
				if board[j][i] != '0':
					tmp.append(board[j][i])

			tmp.reverse()
			for j in range(m - len(tmp)):
				tmp.append('0')
			tmp.reverse()
			
			for j in range(m):
				board[j][i] = tmp[j]

	return answer

print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
print(solution(5, 6, ['AAAAAA', 'BBAATB', 'BBAATB', 'JJJTAA', 'JJJTAA']))
print(solution(4, 5, ['AAAAA', 'AUUUA', 'AUUAA', 'AAAAA']))
print(solution(4, 4, ['ABCD', 'BACE', 'BCDD', 'BCDD']))