import sys
input = sys.stdin.readline

N = int(input())
Map = [[-1] * 2 for _ in range(N)]

for i in range(N):
	root, left, right = map(ord, input().split())

	if chr(left) != '.':
		Map[root - ord('A')][0] = left - ord('A')
	if chr(right) != '.':
		Map[root - ord('A')][1] = right - ord('A')

def pre_order(node=0):
	if node == -1:
		return

	print(chr(node + ord('A')), end='')
	pre_order(Map[node][0])
	pre_order(Map[node][1])

def in_order(node=0):
	if node == -1:
		return

	in_order(Map[node][0])
	print(chr(node + ord('A')), end='')
	in_order(Map[node][1])

def post_order(node=0):
	if node == -1:
		return

	post_order(Map[node][0])
	post_order(Map[node][1])
	print(chr(node + ord('A')), end='')

pre_order();print()
in_order();print()
post_order()