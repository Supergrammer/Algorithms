def solution(logs):
	answer = set()
	solved = {}
	logs = sorted(logs)

	for log in logs:
		log = log.split()
		if not solved.get(log[0]):
			solved[log[0]] = [set(), [-1] * 101]
		solved[log[0]][0].add(int(log[1]))
		if solved[log[0]][1][int(log[1])] < int(log[2]):
			solved[log[0]][1][int(log[1])] = int(log[2])
		
	keys = list(solved.keys())
	for i in range(len(keys)):
		if len(solved[keys[i]][0]) >= 5:
			for j in range(i + 1, len(keys)):
				if len(solved[keys[i]][0]) == len(solved[keys[j]][0]):
					if solved[keys[i]][0] == solved[keys[j]][0]:
						ischeat = True
						for k in solved[keys[i]][0]:
							if solved[keys[i]][1][k] != solved[keys[j]][1][k]:
								ischeat = False; break

						if ischeat:
							answer.update([keys[i], keys[j]])

	answer = sorted(list(answer))
	if not answer:
		return ['None']
	return answer

print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))
print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]))
print(solution(["1901 10 50", "1909 10 50"]))