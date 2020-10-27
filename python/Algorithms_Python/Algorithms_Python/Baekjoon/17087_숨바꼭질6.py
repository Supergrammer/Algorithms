import sys
input = sys.stdin.readline

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def precalc(n):
	return abs(int(n) - S)

N, S = map(int, input().split())
bros = list(map(precalc, input().split()))
d = bros[0]

for i in bros[1:]:
	d = gcd(d, i)
	if d == 1: break

print(d)