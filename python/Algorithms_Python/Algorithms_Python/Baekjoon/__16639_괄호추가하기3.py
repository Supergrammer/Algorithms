import sys
input = sys.stdin.readline

N = int(input())
string = input().strip()

num, oper = [], []
ptr = 0
answer = -sys.maxsize

for i in range(N):
	if i % 2: oper.append(string[i])
	else: num.append(int(string[i]))

N //= 2

def calc(nm, op):
	rtn = nm[0]
	for i in range(len(op)):
		if op[i] == '+': rtn += nm[i + 1]
		elif op[i] == '-': rtn -= nm[i + 1]
		else: rtn *= nm[i + 1]
	return rtn

def bracket(ptr, nm, op):
	if ptr == N:
		global answer
		answer = max(answer, calc(nm, op))
		return

	bracket(ptr + 1, nm + [num[ptr + 1]], op + [oper[ptr]])
	if ptr < N:
		if oper[ptr] == '+': nm[-1] += num[ptr + 1]
		elif oper[ptr] == '-': nm[-1] -= num[ptr + 1]
		else: nm[-1] *= num[ptr + 1]
		bracket(ptr + 1, nm, op)

bracket(0, [num[0]], [])
print(answer)