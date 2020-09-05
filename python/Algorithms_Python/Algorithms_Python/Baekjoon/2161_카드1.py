import sys
input = sys.stdin.readline

N = int(input())
card = [i + 1 for i in range(N)]

while N != 1:
	if N % 2:
		for i in card[:N - 1:2]:
			print(i, end = ' ')
		card = [card[N - 1]] + card[1::2]
		N = N // 2 + 1
	else:
		for i in card[::2]:
			print(i, end = ' ')
		card = card[1::2]
		N //= 2

print(card[0])