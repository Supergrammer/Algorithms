import sys
input = sys.stdin.readline

N = int(input())
stair = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
seq = stair[:]

for _ in range(N - 1):
	seq[0], seq[9] = stair[1], stair[8]
	for i in range(1, 9):
		seq[i] = stair[i - 1] + stair[i + 1]
	stair = seq[:]

print(sum(stair) % 1000000000)