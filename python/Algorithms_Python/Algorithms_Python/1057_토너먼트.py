import sys
input = sys.stdin.readline

N, Kim, Lim = map(int, input().split())
round = 0

while Kim != Lim:
	round += 1
	Kim = Kim // 2 + Kim % 2
	Lim = Lim // 2 + Lim % 2

print(round)