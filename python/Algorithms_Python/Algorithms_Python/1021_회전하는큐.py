from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map = deque([i + 1 for i in range(N)])
List = deque(list(map(int, input().split())))
sum = 0

while List:
	if Map[0] == List[0]:
		Map.popleft()
		List.popleft()
		N -= 1
	else:
		idx = Map.index(List[0])
		if idx >= N - idx:
			Map.rotate(N - idx)
			sum += (N - idx)
		else:
			Map.rotate(-idx)
			sum += idx
print(sum)