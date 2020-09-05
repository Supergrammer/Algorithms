from collections import deque
import sys
input = sys.stdin.readline

def calc():
	Q = deque([A])
	visited = ['' for _ in range(mx)]
	visited[A] = ' '

	while Q:
		size = len(Q)
		while size != 0:
			n = Q.popleft()
			size -= 1
			for i in range(4):
				val, let = move(i, n)
				if check(val) and not visited[val]:
					if val == B: return (visited[n] + let).replace(' ', '')
					Q.append(val)
					visited[val] = visited[n] + let

def move(op, num):
	if op == 0: return num * 2 % mx, 'D'
	elif op == 1: return (num + 9999) % mx, 'S'
	elif op == 2: return num * 10 % mx + int(num / 1000), 'L'
	else: return int(num / 10) + num % 10 * 1000, 'R'

def check(n: int):
	if 0 <= n < 10000:
		return True
	else: return False

T = int(input())
mx = 10000
for _ in range(T):
	A, B = map(int, input().split())
	print(calc())