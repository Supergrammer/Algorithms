import sys

def solution(begin, target, words):
	answer = sys.maxsize

	words = [begin] + words
	canmove = [[0] * len(words) for _ in range(len(words))]
	visited = [0] * len(words)
	visited[0] = 1

	def change(word1, word2):
		cnt = 0
		for i in range(len(word1)):
			if word1[i] != word2[i]:
				cnt += 1
			if cnt > 1: return False
		return True

	def find(num, depth=0):
		if words[num] == target:
			nonlocal answer
			answer = min(answer, depth)
			return

		for i in range(len(canmove[num])):
			if canmove[num][i] and not visited[i]:
				visited[i] = 1
				find(i, depth + 1)
				visited[i] = 0

	for i in range(len(words)):
		for j in range(i + 1, len(words)):
			if change(words[i], words[j]):
				canmove[i][j] = canmove[j][i] = 1

	find(0)
	if answer == sys.maxsize:
		return 0
	return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))