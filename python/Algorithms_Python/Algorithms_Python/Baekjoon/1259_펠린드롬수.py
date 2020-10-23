import sys
input = sys.stdin.readline

while True:
	N = input().strip()
	if N == '0':
		break

	l = len(N) // 2
	isPal = True
	for i in range(l):
		if not N[i] == N[len(N) - i - 1]:
			isPal = False; break

	print('yes' if isPal else 'no')