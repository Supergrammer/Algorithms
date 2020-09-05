import sys
sys.stdin.readline

A, B, C = map(int, input().split())
car = [0 for _ in range(101)]

for _ in range(3):
	fr, to = map(int, input().split())
	for i in range(fr, to):
		car[i] += 1

sum = car.count(1) * A + car.count(2) * B * 2 + car.count(3) * C * 3
print(sum)