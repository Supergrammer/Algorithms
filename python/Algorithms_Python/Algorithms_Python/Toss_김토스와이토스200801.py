import sys
input = sys.stdin.readline

kimToss = list(map(int, input().split()))
leeToss = list(map(int, input().split()))

for i in range(len(kimToss)):
	kimToss[i] -= leeToss[i]
	if kimToss[i] >= 0:
		print(kimToss[i], end=' ')
	else:
		if i != len(kimToss) - 1:
			kimToss[i + 1] += kimToss[i]
		print(0, end=' ')