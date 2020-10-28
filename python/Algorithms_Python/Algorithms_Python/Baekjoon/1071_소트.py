import sys
input = sys.stdin.readline

N = int(input())
ipt = list(map(int, input().split()))
seq = {}
answer = []

if N == 1:
	print(ipt[0])
	sys.exit()

for i in ipt:
	if seq.get(i): seq[i] += 1
	else: seq[i] = 1

arr = sorted(seq.keys())

if len(arr) != 1:
	ptr = 1
	while True:
		if arr[ptr] == arr[ptr - 1] + 1:
			if ptr == len(arr) - 1:
				arr[ptr], arr[ptr - 1] = arr[ptr - 1], arr[ptr]
			else:
				tmp = arr[ptr + 1]
				seq[tmp] -= 1
				if not seq[tmp]:
					del arr[ptr + 1]
				arr.insert(ptr, tmp + 1001)
	
		ptr += 1
		if ptr > len(arr) - 1:
			break

for i in arr:
	if i > 1001:
		print(i - 1001, end=' ')
	else:
		for _ in range(seq[i]):
			print(i, end=' ')

"""
import sys
input = sys.stdin.readline

N = int(input())
seq = sorted(list(map(int, input().split())))
visited = [False] * N
answer = []

def seqsort(arr):
	if len(arr) == N:
		for i in arr:
			print(i, end=' ')
		sys.exit()

	for i in range(N):
		if not visited[i]:
			if arr:
				if arr[-1] != seq[i] - 1:
					arr.append(seq[i]); visited[i] = True
					seqsort(arr)
					arr.pop(); visited[i] = False
			else:
				arr.append(seq[i]); visited[i] = True
				seqsort(arr)
				arr.pop(); visited[i] = False

seqsort([])
"""