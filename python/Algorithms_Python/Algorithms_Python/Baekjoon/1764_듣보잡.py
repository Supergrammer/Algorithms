import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D, B = [], []

for _ in range(N):
	D.append(input().strip())
for _ in range(M):
	B.append(input().strip())

DB = list(set(D) & set(B))
print(len(DB))
print('\n'.join(sorted(DB)))