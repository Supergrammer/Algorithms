def solution(votes, k):
	answer = ''
	
	tmp = {}
	vote = []

	for v in votes:
		if tmp.get(v): tmp[v] += 1
		else: tmp[v] = 1

	for key, val in tmp.items():
		vote.append([key, val])

	vote = sorted(vote, key=lambda x:(-x[1], x[0]))

	voted = 0
	for i in range(k):
		voted += vote[i][1]

	while True:
		voted -= vote[-1][1]
		if voted <= 0:
			return answer
		answer = vote[-1][0]
		vote.pop()

print(solution(["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"], 2))
print(solution(["AAD", "AAA", "AAC", "AAB"], 4))