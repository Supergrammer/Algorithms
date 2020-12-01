import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
Arr = [list(map(int, input().split())) for _ in range(3)]

def operR(R):
	mx = 0
	for i in range(R):
		cnt = [[i, 0] for i in range(101)]
		for j in Arr[i]:
			cnt[j][1] += 1

		cnt = sorted(list(filter(lambda x:x[1] != 0, cnt[1:])), key=lambda x:x[1])
		tmp = []
		for j in range(len(cnt)):
			tmp += cnt[j]
		if len(tmp) > 100:
			tmp = tmp[:100]
		mx = max(mx, len(tmp))
		Arr[i] = tmp

	for i in range(R):
		if len(Arr[i]) < mx:
			Arr[i] += [0] * (mx - len(Arr[i]))

	return

def operC(C):
	mx = 0
	arr = [[] for _ in range(C)]
	for i in range(C):
		for j in range(len(Arr)):
			arr[i].append(Arr[j][i])

	for i in range(C):
		cnt = [[i, 0] for i in range(101)]
		for j in arr[i]:
			cnt[j][1] += 1

		cnt = sorted(list(filter(lambda x:x[1] != 0, cnt[1:])), key=lambda x:x[1])
		tmp = []
		for j in range(len(cnt)):
			tmp += cnt[j]
		if len(tmp) > 100:
			tmp = tmp[:100]
		mx = max(mx, len(tmp))
		arr[i] = tmp

	for i in range(C):
		if len(arr[i]) < mx:
			arr[i] += [0] * (mx - len(arr[i]))

	tmp = [[] for _ in range(len(arr[0]))]
	for i in range(len(arr[0])):
		for j in range(len(arr)):
			tmp[i].append(arr[j][i])
	
	return tmp

r -= 1; c -= 1
time = 0

while True:
	R, C = len(Arr), len(Arr[0])
	if (R > r and C > c and Arr[r][c] == k) or time > 100:
		break
	
	if R >= C: operR(R)
	else: Arr = operC(C)

	time += 1

print(-1 if time > 100 else time)