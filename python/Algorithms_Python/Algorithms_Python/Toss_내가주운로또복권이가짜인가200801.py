import sys
input = sys.stdin.readline

def check():
	prev = lotto[0]

	if not 1 <= prev <= 45 or len(lotto) != 6:
		return 'false'
	for i in range(1, len(lotto)):
		if prev >= lotto[i] or not 1 <= lotto[i] <= 45:
			return 'false'
		prev = lotto[i]
	return 'true'

lotto = list(map(int, input().split()))
print(check())