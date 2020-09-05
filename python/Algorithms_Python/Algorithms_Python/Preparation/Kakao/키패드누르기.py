def solution(numbers, hand):
	answer = ''
	left, right = [3, 0], [3, 2]

	for i in numbers:
		num = []
		if i == 0:
			num = [3, 1]
		else:
			num = [(i - 1) // 3, (i - 1) % 3]

		if num[1] == 0:
			answer += 'L'; left = num
		elif num[1] == 2:
			answer += 'R'; right = num
		else:
			l = abs(num[0] - left[0]) + abs(num[1] - left[1])
			r = abs(num[0] - right[0]) + abs(num[1] - right[1])
			if l > r:
				answer += 'R'; right = num
			elif l < r:
				answer += 'L'; left = num
			else:
				if hand == 'right':
					answer += 'R'; right = num
				else:
					answer += 'L'; left = num

	return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))