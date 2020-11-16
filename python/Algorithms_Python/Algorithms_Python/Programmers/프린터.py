def solution(priorities, location):
	answer = 0

	for i in range(len(priorities)):
		priorities[i] = [priorities[i], False]
	priorities[location][1] = True

	while True:
		answer += 1
		mx, index = -1, -1
		for i in range(len(priorities)):
			if priorities[i][0] > mx:
				mx = priorities[i][0]; index = i

		if priorities[index][1]:
			return answer

		priorities = (priorities[index + 1:] if index < len(priorities) else []) + priorities[:index]

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))