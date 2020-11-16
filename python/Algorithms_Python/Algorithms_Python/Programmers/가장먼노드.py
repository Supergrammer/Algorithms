from collections import deque

def solution(n, edge):
	answer = 0

	graph = {}
	visited = [False] * (n + 1)

	for e in edge:
		if graph.get(e[0]): graph[e[0]].append(e[1])
		else: graph[e[0]] = [e[1]]
		if graph.get(e[1]): graph[e[1]].append(e[0])
		else: graph[e[1]] = [e[0]]

	Q = deque([1])
	visited[1] = True
	dist = 0

	while True:
		size = len(Q)
		dist += 1

		for _ in range(size):
			node = Q.popleft()
			for i in graph[node]:
				if not visited[i]:
					Q.append(i)
					visited[i] = True

		if not Q:
			answer = size
			break

	return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))