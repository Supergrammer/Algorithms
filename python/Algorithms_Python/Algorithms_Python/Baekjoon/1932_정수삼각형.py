import sys
input = sys.stdin.readline

N = int(input())
mem = [0] + list(map(int, input().split())) + [0]

for i in range(N - 1):
	tmp = list(map(int, input().split()))
	for j in range(i + 2):
		tmp[j] += max(mem[j], mem[j + 1])
	mem = [0] + tmp + [0]

print(max(mem))