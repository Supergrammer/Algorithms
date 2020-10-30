import sys
input = sys.stdin.readline

for _ in range(int(input())):
	input()
	seq = list(map(int, input().split()))
	print(min(seq), max(seq))