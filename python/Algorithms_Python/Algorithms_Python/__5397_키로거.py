import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	L = input()
	password = []
	pointer = 0

	for c in L:
		if c == '<':
			if pointer > 0:
				pointer -= 1
		elif c == '>':
			if pointer < len(password):
				pointer += 1
		elif c == '-':
			if pointer > 0:
				del password[pointer - 1]
				pointer -= 1
		else:
			password.insert(pointer, c)
			pointer += 1

	for i in password:
		print(i, end = '')