import sys
input = sys.stdin.readline

while True:
	a, b, c = sorted(list(map(int, input().split())))
	if a == 0: break

	if a ** 2 + b ** 2 == c ** 2:
		print('right')
	else: print('wrong')