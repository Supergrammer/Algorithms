def solution(n, board):
	answer = 0
	arr = []
	pointer = [0, 0]

	def find(num, arr):
		for i in range(n):
			for j in range(n):
				if board[i][j] == num:
					arr.append([i, j])
					return

	for num in range(1, n ** 2 + 1):
		find(num, arr)
		
	for num in arr:
		y, x = abs(pointer[0] - num[0]), abs(pointer[1] - num[1])
		if y > n // 2: y = n - y
		if x > n // 2: x = n - x
		answer += y + x + 1
		pointer = num

	return answer

print(solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]))
print(solution(2, [[2, 3], [4, 1]]))
print(solution(4, [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]]))