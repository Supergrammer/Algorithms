N = int(input())
a, b, sum = 0, 0, 5000

while(N >= 0):
	if N % 3 == 0:
		b = N / 3
		sum = min(a + b, sum)
	N -= 5
	a += 1

print(int(-1 if sum == 5000 else sum))