import sys
input = sys.stdin.readline

N = int(input()) % 1500000
Fibo = [0] * 1500000
Fibo[1] = 1

for i in range(2, N + 1):
	Fibo[i] = (Fibo[i - 1] + Fibo[i - 2]) % 1000000

print(Fibo[N])