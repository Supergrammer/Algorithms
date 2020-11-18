def solution(n, times):
	answer = 0

	left, right = 1, 1000000000

	def calc(mid):
		cnt = 0
		for time in times:
			cnt += mid // time
		return cnt

	while left < right:
		mid = (left + right) // 2
		cnt = calc(mid)

		if n > cnt: left = mid + 1
		else: right = mid - 1

		answer = left

	while calc(answer) < n:
		answer += 1

	return answer

print(solution(6, [7, 10]))
print(solution(1000, [7, 10, 20]))