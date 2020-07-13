import sys
input = sys.stdin.readline

A, B = map(str, input().split())
lenA, lenB = len(A), len(B)
mn = 50

for i in range(lenB - lenA + 1):
	tmp = ' ' * i + A + ' ' * (lenB - lenA - i)
	cnt = 0
	for j in range(lenB):
		if tmp[j] != ' ' and tmp[j] != B[j]:
			cnt += 1
	mn = min(mn, cnt)

print(mn)