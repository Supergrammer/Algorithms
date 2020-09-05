import sys
input = sys.stdin.readline

M = int(input())
ball = [1, 0, 0]

for _ in range(M):
	tmp = list(map(int, input().split()))
	ball[tmp[0] - 1], ball[tmp[1] - 1] = ball[tmp[1] - 1], ball[tmp[0] - 1]

print(ball.index(1) + 1)