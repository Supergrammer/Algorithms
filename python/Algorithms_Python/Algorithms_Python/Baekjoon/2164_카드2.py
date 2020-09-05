import sys
input = sys.stdin.readline

N = int(input())
card = [i + 1 for i in range(N)]

while N != 1:
	if N % 2:
		card = [card[N - 1]] + card[1::2]
		N = N // 2 + 1
	else:
		card = card[1::2]
		N //= 2

print(card[0])