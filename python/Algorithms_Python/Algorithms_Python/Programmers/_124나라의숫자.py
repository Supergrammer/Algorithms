def solution1(n):
	answer = ''

	while n > 3:
		div = n // 3
		if div == 1:
			div += 1
		n -= (div - 1) * 3
		answer += str(n % 3)
	answer += str(n)
	answer = list(answer)

	for i in range(len(answer)):
		if answer[i] == '3':
			answer[i] = '4'

	return ''.join(answer)

def solution2(n):
	answer = ''
	arr3 = []

	for i in range(18, -1, -1):
		arr3.append(3 ** i)

	for i in arr3:
		if i > n:
			continue
		
		cnt = 0
		while i <= n:
			n -= i; cnt += 1
		answer += str(cnt)

	return answer

def solution3(n):
	answer = ''
	num, pow = 581130732, 18

	def answerapp(n):
		if n == 1: return '1'
		elif n == 2: return '2'
		elif n == 3: return '4'

	if n <= 3:
		return answerapp(n)

	while True:
		if num <= n < num + 3 ** (pow + 1):
			div = n // 3 ** pow
			answer += answerapp(div)
			n -= (3 ** pow) * div
		
		num -= 3 ** pow
		pow -= 1

		if num < 0 or n == 0:
			return answer

print(solution(39))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(17))