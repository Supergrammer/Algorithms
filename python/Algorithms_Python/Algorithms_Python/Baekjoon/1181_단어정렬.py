import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
	tmp = input().strip()
	heapq.heappush(arr, ((len(tmp), tmp), tmp))

prv = ''
for i in range(len(arr)):
	tmp = heapq.heappop(arr)[1]
	if prv != tmp:
		print(tmp)
	prv = tmp