def solution(new_id):
	answer = new_id

	answer = answer.lower()

	tmp = ''
	prv = ''
	for c in answer:
		if 'a' <= c <= 'z' or '0' <= c <= '9' or c in '-_.':
			if prv == '.' and c == '.':
				continue
			tmp += c
			prv = c
	answer = tmp

	answer = answer.strip('.')

	if answer == '':
		answer += 'a'

	if len(answer) >= 16:
		answer = answer[:15]
		answer = answer.rstrip('.')

	while len(answer) <= 2:
		answer += answer[-1]

	return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))