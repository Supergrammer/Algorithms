from collections import deque

def solution(n, computers):
	answer = 0
	visited = [False] * n

	def find(num):
		Q = deque([num])
		visited[num] = True

		while Q:
			num = Q.popleft()

			for i in range(n):
				if computers[num][i] and not visited[i]:
					Q.append(i)
					visited[i] = True

	for i in range(n):
		if not visited[i]:
			find(i)
			answer += 1

	return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))