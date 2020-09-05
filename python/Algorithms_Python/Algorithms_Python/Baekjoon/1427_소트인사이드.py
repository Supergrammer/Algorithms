import sys
input = sys.stdin.readline

N = list(input().strip())
N.sort(reverse=True)

for n in N:
	print(n, end='')
print()