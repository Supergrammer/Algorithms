import re

def calc(exp, ord, oper):
	for o in ord:
		op = []
		for i in range(len(oper)):
			if oper[i] == o:
				op.append(i)
		
		for i in reversed(op):
			oper.pop(i)
		
		cnt = 0
		for i in op:
			tmp = i - cnt 
			if o == '*':
				exp[tmp] *= exp[tmp + 1]
			elif o == '+':
				exp[tmp] += exp[tmp + 1]
			else:
				exp[tmp] -= exp[tmp + 1]
			cnt += 1
			exp.pop(tmp + 1)

	return abs(exp[0])

def solution(expression):
	answer = 0
	operator = []
	order = ['*+-', '*-+', '+*-', '+-*', '-*+', '-+*']

	for c in expression:
		if c in '*+-':
			operator.append(c)
	expression = list(map(int, re.split('[*,+,-]', expression)))

	for ord in order:
		answer = max(answer, calc(expression[:], ord, operator[:]))

	return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))