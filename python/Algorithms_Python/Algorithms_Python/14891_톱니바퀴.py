from collections import deque
import sys
input = sys.stdin.readline

def Rotate(num, dir):
	done[num] = True
	if num > 0 and Map[num][6] != Map[num - 1][2] and not done[num - 1]:
		Rotate(num - 1, -dir)
	if num < 3 and Map[num][2] != Map[num + 1][6] and not done[num + 1]:
		Rotate(num + 1, -dir)
	Map[num].rotate(dir)

def calcScore():
	score = 0
	for i in range(4):
		score += int(Map[i][0]) * (2 ** i)
	return score

Map = []
for _ in range(4):
	Map.append(deque(list(input().strip())))
K = int(input())
for _ in range(K):
	num, dir = map(int, input().split())
	done = [False for _ in range(4)]
	Rotate(num - 1, dir)

print(calcScore())