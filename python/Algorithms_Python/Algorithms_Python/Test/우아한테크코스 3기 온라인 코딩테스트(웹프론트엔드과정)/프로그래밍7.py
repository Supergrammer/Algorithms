def solution(n, horizontal):
	answer = [[-1] * n for _ in range(n)]
	time = 0

	arr = []
	for i in range((n - 1) * 2 + 1):
		tmp = []
		for j in range(n - abs(n - i - 1)):
			tmp.append(time)
			if j != n - abs(n - i - 1) - 1:
				time += 2
		time += 1

		if (not horizontal and i % 2 == 1) or (horizontal and i % 2 == 0):
			tmp.reverse()

		if i < n - 1: tmp = tmp + [-1] * (n - len(tmp))
		else: tmp = [-1] * (n - len(tmp)) + tmp
		arr.append(tmp)

	for i in range(n):
		tmp = []

		for j in range((n - 1) * 2 + 1):
			if arr[j][i] != -1:
				tmp.append(arr[j][i])
		
		for j in range(n):
			answer[i][j] = tmp[j]

	return answer

print(solution(4, True))
print(solution(5, False))
print(solution(7, True))