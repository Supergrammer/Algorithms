def solution(m, k):
	m = list(m)
	pointer = 0

	for c in k:
		while True:
			try:
				if m[pointer] == c:
					m[pointer] = m[pointer].upper()
					break
			except IndexError:
				break

			pointer += 1

	for c in m:
		if 'A' <= c <= 'Z':
			m.remove(c)

	return ''.join(m)

print(solution("kkaxbycyz", "abc"))
print(solution("acbbcdc", "abc"))
print(solution("aabcb", "ab"))