def solution(clothes):
	answer = 0
	clothesmap = {}

	for cloth in clothes:
		if clothesmap.get(cloth[1]):
			clothesmap[cloth[1]] += 1
		else:
			clothesmap[cloth[1]] = 1

	val = list(clothesmap.values())
	visited = [0] * len(val)

	def DFS(depth=0):
		if depth == len(val):
			nonlocal answer
			sum = 1
			for i in range(len(val)):
				if visited[i]: sum *= val[i]
			answer += sum
			return

		DFS(depth + 1)
		visited[depth] = 1
		DFS(depth + 1)

	DFS()
	return answer - 1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))