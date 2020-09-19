def solution(N, stages):
	answer = []
	Map = [0] * (N + 2)
	denom = [0] * (N + 2)
	dict = {}

	for i in stages:
		Map[i] += 1

	denom[N + 1] = Map[N + 1]
	for i in range(len(Map) - 2, 0, -1):
		denom[i] = Map[i] + denom[i + 1]
		if denom[i] != 0:
			dict[i] = Map[i] / denom[i]
		else: dict[i] = 0

	tmp = sorted(dict.items(), key=lambda x: x[1])
	for key, val in tmp:
		answer.append(key)
	answer.reverse()

	return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))