def solution(prices):
	answer = [0] * len(prices)
	stack = []

	for i in range(len(prices)):
		if stack and prices[stack[-1]] > prices[i]:
			while True:
				if prices[stack[-1]] <= prices[i]:
					break
				tmp = stack.pop()
				answer[tmp] = i - tmp
		stack.append(i)

	while stack:
		tmp = stack.pop()
		answer[tmp] = len(prices) - tmp - 1

	return answer

print(solution([1, 2, 3, 2, 3]))
print(solution([1, 2, 3, 2, 3, 5, 7, 3, 5, 1, 4, 6, 3, 2]))