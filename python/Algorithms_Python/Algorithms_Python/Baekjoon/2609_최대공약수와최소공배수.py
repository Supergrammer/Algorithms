import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a, b)

print(gcd(A, B))
print(lcm(A, B))