def solution(penter, pexit, pescape, data):
	answer = ''
	length = len(penter)
	arr = [penter, pexit, pescape]

	for i in range(len(data) // length):
		bit = data[length * i:length * (i + 1)]
		if bit in arr:
			answer += pescape
		answer += bit

	answer = penter + answer + pexit
	return answer

print(solution("1100", "0010", "1001", "1101100100101111001111000000"))
print(solution("10", "11", "00", "00011011"))