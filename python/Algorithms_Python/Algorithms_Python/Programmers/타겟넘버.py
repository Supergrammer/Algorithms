from collections import deque

def solution(numbers, target):
	answer = 0

	visited = [0] * 2001
	visited[1000 + numbers[0]] = 1
	visited[1000 - numbers[0]] = 1

	for i in range(1, len(numbers)):
		next = [0] * 2001
		for j in range(2001):
			if visited[j] != 0:
				next[j + numbers[i]] += visited[j]
				next[j - numbers[i]] += visited[j]

		visited = next

	answer = visited[target + 1000]
	return answer

print(solution([1, 1, 1, 1, 1], 3))