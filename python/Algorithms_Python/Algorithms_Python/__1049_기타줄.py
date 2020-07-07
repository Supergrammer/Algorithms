import sys
input = sys.stdin.readline

N, M = map(int, input().split())
min6, min1 = sys.maxsize, sys.maxsize
for _ in range(M):
	tmp = list(map(int, input().split()))
	min6 = min(min6, tmp[0])
	min1 = min(min1, tmp[1])

def calcprice():
	if min1 * 6 < min6:
		return N * min1
	elif min6 < min1:
		return ((N // 6) * min6 + min6 if N % 6 else 0)
	else:
		return ((N // 6) * min6 + min(min6 ,(N % 6) * min1))

print(calcprice())