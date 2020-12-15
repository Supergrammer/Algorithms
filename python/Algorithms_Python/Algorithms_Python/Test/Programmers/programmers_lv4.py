def solution1(sticker):
	if len(sticker) <= 3:
		return max(sticker)

	arr1, arr2 = sticker[:-1], sticker[1:]

	def DP(arr):
		memoi = [0] * len(arr)
		memoi[0], memoi[1], memoi[2] = arr[0], arr[1], arr[0] + arr[2]

		for i in range(3, len(arr)):
			memoi[i] = arr[i] + max(memoi[i - 2], memoi[i - 3])

		rtn = max(memoi[len(arr) - 1], memoi[len(arr) - 2])
		return rtn

	answer = max(DP(arr1), DP(arr2))
	return answer

print(solution1([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution1([1, 3, 2, 5, 4]))

from collections import deque
import heapq

def solution2(land, height):
	dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	island = [[0] * len(land) for _ in range(len(land))]
	bridges = []
	answer = 0

	def getIsland():
		visited = [[False] * len(land) for _ in range(len(land))]
		num = 1

		def BFS(arr, num):
			Q = deque([arr])
			
			while Q:
				y, x = Q.popleft()
				h = land[y][x]

				for dy, dx in dir:
					iy, ix = y + dy, x + dx
					if 0 <= iy < len(land) and 0 <= ix < len(land) and not visited[iy][ix]\
						and abs(land[iy][ix] - h) <= height:
						Q.append([iy, ix])
						island[iy][ix] = num
						visited[iy][ix] = True
		
		for i in range(len(land)):
			for j in range(len(land)):
				if not visited[i][j]:
					visited[i][j] = True
					island[i][j] = num
					BFS([i, j], num)
					num += 1

		return num

	def bridge():
		visited = [[False] * len(land) for _ in range(len(land))]

		for i in range(len(land)):
			for j in range(len(land)):
				for dy, dx in dir:
					iy, ix = i + dy, j + dx
					if 0 <= iy < len(land) and 0 <= ix < len(land)\
						and island[i][j] != island[iy][ix]:
						heapq.heappush(bridges, [abs(land[i][j] - land[iy][ix]), island[i][j], island[iy][ix]])

	def kruskal():
		cnt, answer = 0, 0
		parent = [i for i in range(area)]

		def union(a, b):
			a, b = find(a), find(b)
			parent[b] = a

		def find(a):
			if parent[a] == a:
				return parent[a]

			parent[a] = find(parent[a])
			return parent[a]

		while True:
			if not bridges:
				return answer

			length, fr, to = heapq.heappop(bridges)
			if find(fr) != find(to):
				union(fr, to)
				cnt += 1
				answer += length

			if cnt == area - 2:
				return answer

	area = getIsland()
	bridge()
	answer = kruskal()

	return answer

print(solution2([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution2([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))