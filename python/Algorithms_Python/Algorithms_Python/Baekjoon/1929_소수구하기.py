"""
from math import sqrt
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(range(M, N + 1))
prime = list(range(2, int(sqrt(N)) + 2))

for i in range(2, int(sqrt(prime[-1])) + 2):
	for j in range(len(prime)):
		if i == prime[j]: continue
		if prime[j] % i == 0: prime[j] = 0
	prime = list(filter(lambda x:x != 0, prime))

for i in prime:
	for j in range(len(arr)):
		if i == arr[j]: continue
		if arr[j] % i == 0: arr[j] = 0
	arr = list(filter(lambda x:x != 0, arr))

for i in arr:
	if i == 1: continue
	print(i)
"""

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
prime = [True] * (N + 1)
prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
	if prime[i]:
		prime[i ** 2::i] = [False] * ((N - i ** 2) // i + 1)

for i in range(M, N + 1):
	if prime[i]:
		print(i)