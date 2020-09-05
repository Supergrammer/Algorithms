from collections import deque
import itertools
import sys
input = sys.stdin.readline

def solution1():
	while True:
		M = list(map(int, input().split()))
		if M[0] == 0:
			return

		M.pop(0)
		com = list(itertools.combinations(M, 6))
		for i in com:
			for j in i:
				print(j, end=' ')
			print()
		print()

out = []
def combination(arr: []):
	if len(out) == 6:
		for i in out:
			print(i, end=' ')
		print()
		return
	if len(arr) + len(out) < 6:
		return

	for i in range(len(arr)):
		out.append(arr[i])
		combination(arr[i+1:])
		out.pop()		

def solution2():
	while True:
		M = list(map(int, input().split()))
		if M[0] == 0:
			return
		M.pop(0)

		combination(M)
		print()

# solution1()
solution2()