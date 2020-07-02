from collections import deque
import itertools
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map, Per = [], []
Q = deque([])

def BFS(arr: [], q: []):
	visited = [[False for x in range(M)] for y in range(N)]
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]	
	while q:
		y, x = q.popleft()
		for dy, dx in dir:
			iy, ix = y + dy, x + dx
			if 0 <= iy < N and 0 <= ix < M and \
				arr[iy][ix] == 0 and not visited[iy][ix]:
				q.append([iy, ix])
				arr[iy][ix] = 2
				visited[iy][ix] = True

def calculation(arr: []):
	cnt = N * M
	for i in range(N):
		cnt -= arr[i].count(1)
		cnt -= arr[i].count(2)
	return cnt

def solution():
	mx = 0
	for i in range(N):
		Map.append(list(map(int, input().split())))

	for y in range(N):
		for x in range(M):
			if Map[y][x] == 0:
				Per.append([y, x])
			elif Map[y][x] == 2:
				Q.append([y, x])
	
	P = list(itertools.combinations(Per, 3))
	for i in P:
		Copy = copy.deepcopy(Map)
		CQ = copy.deepcopy(Q)
		for j in i:
			Copy[j[0]][j[1]] = 1
			if j[0] == 1 and j[1] == 0:
				pass

		BFS(Copy, CQ)
		mx = max(mx, calculation(Copy))
	
	return mx

print(solution())