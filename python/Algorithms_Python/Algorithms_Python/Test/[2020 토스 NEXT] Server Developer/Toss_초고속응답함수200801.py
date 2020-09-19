import sys
input = sys.stdin.readline

hashmap = {}
inp = list(map(int, input().split()))

for i in inp:
	try:
		print(hashmap[i], end=' ')
	except KeyError:
		hashmap[i] = compute(i)
		print(hashmap[i], end=' ')