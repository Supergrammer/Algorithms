import sys
input = sys.stdin.readline

N = int(input())

ptr = 1
stack = []
history = []
isable = True

for _ in range(N):
	tmp = int(input())
	if tmp >= ptr:
		stack += list(range(ptr, tmp))
		for _ in range(tmp - ptr):
			history.append('+')
		history.append('+')
		history.append('-')
		ptr = tmp + 1
	else:
		if stack[-1] == tmp:
			stack.pop()
			history.append('-')
		else:
			isable = False
			break

if isable:
	print('\n'.join(history))
else:
	print('NO')