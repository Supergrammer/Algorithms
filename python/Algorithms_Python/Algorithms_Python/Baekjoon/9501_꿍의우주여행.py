import sys
input = sys.stdin.readline

for _ in range(int(input())):
	N, D = map(int, input().split())
	answer = 0
	for i in range(N):
		v, f, c = map(int, input().split())
		if D * c / v <= f:
			answer += 1
	print(answer)