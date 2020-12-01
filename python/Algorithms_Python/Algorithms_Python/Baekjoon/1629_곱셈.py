import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
memoi = [0] * 32
memoi[1] = A

for i in range(2, 32):
	memoi[i] = memoi[i - 1] ** 2 % C

B = bin(B)[2:]
answer = 1

for i in range(len(B)):
	if int(B[i]):
		answer = answer * memoi[i] % C

print(answer)