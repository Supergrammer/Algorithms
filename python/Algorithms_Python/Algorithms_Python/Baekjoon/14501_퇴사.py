import sys
input = sys.stdin.readline

N = int(input())
TP, mem = [], [0] * (N + 1)

for i in range(N):
	TP.append(list(map(int, input().split())))

mx = 0
for i in range(N):
	mx = max(mx, mem[i])

	if i + TP[i][0] > N:
		continue

	if mem[i + TP[i][0]] < TP[i][1] + mx:
		mem[i + TP[i][0]] = TP[i][1] + mx

print(max(mem))