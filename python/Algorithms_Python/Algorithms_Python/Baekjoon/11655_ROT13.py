import sys
input = sys.stdin.readline

S = list(input().strip('\n'))

def check(c):
	if not (65 <= c <= 90 or 97 <= c <= 122):
		return False
	return True

for i in range(len(S)):
	if not check(ord(S[i])):
		continue

	tmp = ord(S[i]) + 13
	if 91 <= tmp <= 103 or 123 <= tmp <= 135:
		tmp -= 26
	S[i] = chr(tmp)

for c in S:
	print(c, end='')
print()