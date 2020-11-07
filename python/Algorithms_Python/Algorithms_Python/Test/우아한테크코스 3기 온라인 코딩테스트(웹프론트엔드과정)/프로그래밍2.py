def solution(s, op):
	answer = []
	for i in range(1, len(s)):
		s1, s2 = int(s[:i]), int(s[i:])
		if op == '+': answer.append(s1 + s2)
		elif op == '-': answer.append(s1 - s2)
		else: answer.append(s1 * s2)

	return answer

print(solution("1234", "+"))
print(solution("987987", "-"))
print(solution("31402", "*"))