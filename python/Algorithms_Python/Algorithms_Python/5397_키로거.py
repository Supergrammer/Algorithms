import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	L = input().strip()
	left, right = [], []

	for c in L:
		if c == '<':
			if left:
				right.append(left.pop())
		elif c == '>':
			if right:
				left.append(right.pop())
		elif c == '-':
			if left:
				left.pop()
		else:
			left.append(c)
	
	left += list(reversed(right))
	print(''.join(left))