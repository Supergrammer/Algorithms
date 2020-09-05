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