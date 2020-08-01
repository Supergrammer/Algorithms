import sys
input = sys.stdin.readline

data = list(map(int, input().strip().replace(';', '').split()))
pointer = data.pop(0)
copy = []

while True:
	if data[pointer] == 0:
		pointer = data[pointer + 1]
		copy.append(0)
		copy.append(len(copy) + 1)
	else:
		copy.append(1)
		copy.append(data[pointer + 1])
		break

for i in range(8 - len(copy)):
	copy.append(0)

print('0;', end=' ')
for i in copy:
	print(i, end=' ')