def solution(money):
	answer = 0

	def dp(money:[]):
		memoi = [0] * len(money)
		memoi[0], memoi[1], memoi[2] = money[0], money[1], max(money[0] + money[2], money[1])

		for i in range(3, len(money)):
			memoi[i] = money[i] + max(memoi[i - 2], memoi[i - 3])

		return max(memoi[len(money) - 1], memoi[len(money) - 2])

	if len(money) == 3:
		return max(money)

	answer = max(dp(money[:-1]), dp(money[1:]))
	return answer

print(solution([1, 2, 3, 1]))