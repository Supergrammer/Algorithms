import sys
input = sys.stdin.readline

X = int(input())
cnt = 0

while X != 0:
	cnt += X % 2
	X //= 2

print(cnt)