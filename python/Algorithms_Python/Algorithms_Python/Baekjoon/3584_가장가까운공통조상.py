import sys
input = sys.stdin.readline

for _ in range(int(input())):
	N = int(input())
	tree = [-1] * (N + 1)
	isancestor = [False] * (N + 1)

	for i in range(N - 1):
		parent, child = map(int, input().split())
		tree[child] = parent

	A, B = map(int, input().split())

	while True:
		isancestor[A] = True
		if tree[A] == -1:
			break
		A = tree[A]

	while True:
		if isancestor[B] == True:
			print(B); break
		B = tree[B]