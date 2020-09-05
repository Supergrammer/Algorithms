import sys
input = sys.stdin.readline

N = int(input())
fibonacci = [0, 1, 2] + [0] * 1000

for i in range(3, N + 1):
	fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 10007

print(fibonacci[N])