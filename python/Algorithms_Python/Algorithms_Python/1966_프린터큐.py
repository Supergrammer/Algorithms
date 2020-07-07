import sys
input = sys.stdin.readline

def solution(m: int):
	rst = 1
	while True:
		mx = max(Q)
		if Q[0] == mx:
			if m == 0: return rst
			Q.pop(0)
			m -= 1; rst += 1
		else:
			if m == 0:
				m = len(Q)
			Q.append(Q.pop(0)); m -= 1

T = int(input())
for _ in range(T):
	N, M = map(int, input().split())
	Q = list(map(int, input().split()))
	print(solution(M))