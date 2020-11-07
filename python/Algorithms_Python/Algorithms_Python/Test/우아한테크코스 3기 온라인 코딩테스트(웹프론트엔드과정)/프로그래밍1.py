def solution(grades, weights, threshold):
	answer = 0
	for i in range(len(grades)):
		score = 0
		if grades[i] == "A+": score = 10
		elif grades[i] == "A0": score = 9
		elif grades[i] == "B+": score = 8
		elif grades[i] == "B0": score = 7
		elif grades[i] == "C+": score = 6
		elif grades[i] == "C0": score = 5
		elif grades[i] == "D+": score = 4
		elif grades[i] == "D0": score = 3
		else: score = 0

		answer += score * weights[i]

	answer -= threshold
	return answer

print(solution(["A+","D+","F","C0"], [2,5,10,3], 50))
print(solution(["B+","A0","C+"], [6,7,8], 200))