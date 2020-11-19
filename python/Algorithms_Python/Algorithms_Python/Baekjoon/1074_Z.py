import sys
input = sys.stdin.readline

answer = 0
N, r, c = map(int, input().split())

def find(N, r, c):
	if N == 0: return

	global answer
	mid = 2 ** (N - 1)

	if 0 <= r < mid:
		if 0 <= c < mid: pass
		else:
			answer += mid ** 2
			c -= mid
	else:
		if 0 <= c < mid:
			answer += mid ** 2 * 2
		else:
			answer += mid ** 2 * 3
			c -= mid
		r -= mid

	find(N - 1, r, c)

find(N, r, c)
print(answer)