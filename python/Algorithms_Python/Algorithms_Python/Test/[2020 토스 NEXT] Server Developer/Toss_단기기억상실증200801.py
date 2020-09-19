import sys
input = sys.stdin.readline

inp = list(map(str, input().split()))

for i in range(len(inp)):
	mem = []
	for j in range(i, -1, -1):
		if inp[j] in mem:
			continue

		mem.append(inp[j])
		if len(mem) == 5:
			break
	
	for i in range(len(mem)):
		print(mem[i], end=' ')
	print()