def solution(n, groups):
	answer = 0

	groups = sorted(groups, key=lambda x:(x[0], -x[1]))

	ptr = 1

	for i in range(len(groups)):
		if ptr <= groups[i][1]:
			if ptr < groups[i][0]:
				answer += groups[i][0] - ptr
			ptr = groups[i][1] + 1
			answer += 1
	if ptr < n:
		answer += n - ptr + 1
	return answer

print(solution(10, [[1, 5],[2, 7],[4, 8],[3, 6]]))
print(solution(7, [[6, 7],[1, 4],[2, 4]]))
print(solution(100, [[1, 50],[1,100],[51, 100]]))