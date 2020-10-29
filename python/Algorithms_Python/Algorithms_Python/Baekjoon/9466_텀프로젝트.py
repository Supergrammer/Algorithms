import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

for _ in range(int(input())):
	N = int(input())
	student = [0] + list(map(int, input().split()))
	iscycled = [False] * (N + 1)
	visited = [False] * (N + 1)
	checked = [False] * (N + 1)

	def iscycle(now):
		if visited[now]: return now
		if checked[now]: return 0

		visited[now] = True
		checked[now] = True

		start = iscycle(student[now])
		visited[now] = False

		if start:
			iscycled[now] = True
			if start != now:
				return start
		return 0

	for i in range(1, N + 1):
		if not checked[i]:
			iscycle(i)

	print(iscycled[1:].count(False))

"""
import sys
input = sys.stdin.readline

def cycle(n, start, Q: []):
	Q.append(n)
	visited[n] = True

	if len(Q) > 0 and student[n] == start:
		return
	
	if visited[student[n]]:
		nocycle.extend(Q)
		return

	cycle(student[n], start, Q)

T = int(input())
for _ in range(T):
	N = int(input())
	student = [0] + list(map(int, input().split()))
	nocycle = []
	visited = [False for _ in range(N + 1)]
	
	for i in range(N + 1):
		if student[i] == i:
			visited[i] = True

	for i in range(N + 1):
		if not visited[i]:
			cycle(i, i, [])

	print(len(nocycle))
"""