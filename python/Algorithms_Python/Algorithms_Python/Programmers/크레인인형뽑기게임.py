def solution(board, moves):
	answer = 0
	bucket = []

	for i in moves:
		for j in range(len(board)):
			if board[j][i - 1] != 0:
				bucket.append(board[j][i - 1])
				board[j][i - 1] = 0
				break

		while True:
			prev = 0
			flag = False
			for i in range(len(bucket)):
				if prev == bucket[i]:
					bucket.pop(i)
					bucket.pop(i - 1)
					answer += 2
					flag = True
					break
				prev = bucket[i]

			if not flag:
				break
	return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))