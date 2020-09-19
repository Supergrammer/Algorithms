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

def solution(n):
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

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(12))