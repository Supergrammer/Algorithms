import sys
input = sys.stdin.readline

string = input().strip()

for i in range(len(string) // 10):
	print(string[i * 10:(i + 1) * 10])
print(string[len(string) // 10 * 10:])