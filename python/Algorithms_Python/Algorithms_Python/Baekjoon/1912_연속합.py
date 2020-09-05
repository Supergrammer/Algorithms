import sys
input = sys.stdin.readline

N = int(input())
Seq = list(map(int, input().split()))

for i in range(1, len(Seq)):
	if Seq[i - 1] > 0:
		Seq[i] += Seq[i - 1]

print(max(Seq))