from itertools import combinations

tree = dict()

def prune(arr):
	step = []
	mn = 50

	for i in range(len(arr)):
		try:
			step.extend(tree[arr[i]])
		except KeyError:
			continue

	if len(step) > 1:
		comb = list(combinations(step, len(step) - 1))
		for com in comb:

			mn = min(mn, prune(list(com)))
		return len(arr) + mn
	else:
		return len(arr)

def solution(n, edges):
	answer = 0
	global tree

	for edge in edges:
		try:
			tree[edge[0]].append(edge[1])
		except KeyError:
			tree[edge[0]] = [edge[1]]

	answer = prune([0])
	return answer

print(solution(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))
tree = dict()
print(solution(14, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]))
tree = dict()
print(solution(10, [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]))