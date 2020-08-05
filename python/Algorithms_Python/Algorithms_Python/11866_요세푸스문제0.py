from collections import deque
import sys
input = sys.stdin.readline

# 1
N, K = map(int, input().split())
Map = [0] * (N + 1)
pointer = 0

print('<', end='')
for i in range(N):
	counter = 0
	while counter != K:
		pointer += 1
		if pointer > N:
			pointer -= N
		if Map[pointer] == 0:
			counter += 1

	Map[pointer] = 1
	if i == N - 1:
		print(pointer, end='')
	else:
		print(pointer, end=', ')
print('>')

# 2
N, K = map(int, input().split())
Q = deque([i + 1 for i in range(N)])

print('<', end='')
for i in range(N):
	for j in range(K - 1):
		Q.append(Q.popleft())
	
	if i == N - 1:
		print(Q.popleft(), end='')
	else:
		print(Q.popleft(), end=', ')
print('>')

# 3
N, K = map(int, input().split())
