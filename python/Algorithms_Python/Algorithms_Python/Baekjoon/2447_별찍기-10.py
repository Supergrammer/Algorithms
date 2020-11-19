import sys
input = sys.stdin.readline

N = int(input())

def draw(arr:[]):
	length = len(arr)

	for i in range(length):
		arr.append(arr[i])

	for i in range(length, length * 2):
		arr[i - length] *= 3
		arr[i] = arr[i] + ' ' * length + arr[i]

	for i in range(length):
		arr.append(arr[i])

	return arr

def star(N):
	if N == 1:
		return ['*']
	return draw(star(N // 3))

for row in star(N):
	print(row)