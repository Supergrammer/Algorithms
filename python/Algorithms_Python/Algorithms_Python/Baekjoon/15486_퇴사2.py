import sys
input = sys.stdin.readline

N = int(input())
mem = [0] * (N + 1)

mx = 0
for i in range(N):
	T, P = map(int, input().split())
	mx = max(mx, mem[i])

	if i + T > N:
		continue

	if mem[i + T] < P + mx:
		mem[i + T] = P + mx

print(max(mem))