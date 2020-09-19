import sys
input = sys.stdin.readline

def check():
	prev = string[0]
	if prev not in ['1', '2']:
		return 'false'

	for i in range(1, len(string)):
		if string[i] not in ['1', '2']:
			return 'false'
		if prev == '1' and string[i] == '1':
			return 'false'
		prev = string[i]

	if string[i] == '1':
		return 'false'
	return 'true'

string = list(input())

print(check())