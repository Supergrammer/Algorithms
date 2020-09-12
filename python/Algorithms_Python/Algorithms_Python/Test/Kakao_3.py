def solution(info, query):
	answer = []
	lang, job, exp, food = {}, {}, {}, {}
	score = []

	for i in range(len(info)):
		tmp = list(map(str, info[i].split()))
		for j in [[lang, 0], [job, 1], [exp, 2], [food, 3]]:
			try: j[0][tmp[j[1]]].append(i)
			except KeyError: j[0][tmp[j[1]]] = [i]
		score.append(tmp[4])

	score = list(map(int, score))

	for i in range(len(query)):
		tmpset = {}
		tmp = list(map(str, query[i].split()))
		for j in range(len(tmp) - 1, -1, -1):
			if tmp[j] == 'and':
				tmp.pop(j)

		if tmp[0] == '-': tmpset = set(range(len(info)))
		else: tmpset = set(lang[tmp[0]])

		for j in [[lang, 0], [job, 1], [exp, 2], [food, 3]]:
			if tmp[j[1]] == '-':
				continue
			tmpset = tmpset & set(j[0][tmp[j[1]]])

		result = len(tmpset)
		for i in tmpset:
			if score[i] < int(tmp[4]):
				result -= 1

		answer.append(result)

	return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
			   ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
