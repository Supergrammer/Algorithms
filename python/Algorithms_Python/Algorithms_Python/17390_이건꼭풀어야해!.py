import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
A.sort()
for i in range(1, len(A)):
	A[i] += A[i - 1]

for _ in range(Q):
	fr, to = map(int, input().split())
	print(A[to] - A[fr - 1])