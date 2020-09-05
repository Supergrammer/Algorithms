import sys
input = sys.stdin.readline

mx, now = 0, 0

for _ in range(4):
	getoff, geton = map(int, input().split())
	now -= getoff
	mx = max(mx, now)
	now += geton
	mx = max(mx, now)

print(mx)