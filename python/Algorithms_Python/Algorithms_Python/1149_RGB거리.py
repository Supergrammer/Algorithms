import sys
input = sys.stdin.readline

N = int(input())
cost = list(map(int, input().split()))

for _ in range(N - 1):
	next = list(map(int, input().split()))
	next[0] += min(cost[1], cost[2])
	next[1] += min(cost[0], cost[2])
	next[2] += min(cost[0], cost[1])
	cost = next
	
print(min(cost))