from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Q = deque([])

for _ in range(N):
	ipt = input().split()
	op = ipt[0]

	if len(ipt) > 1:
		Q.appendleft(ipt[1])
	elif op[0] == 's':
		print(len(Q))
	elif op[0] == 'e':
		print(0 if Q else 1)
	elif op[0] == 'f':
		print(Q[-1] if Q else -1)
	elif op[0] == 'b':
		print(Q[0] if Q else -1)
	else:
		print(Q.pop() if Q else -1)