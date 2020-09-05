import sys
input = sys.stdin.readline

def ramp(arr: []):
	check = [False for _ in range(N)]
	for i in range(N - 1):
		try:
			if arr[i] - arr[i + 1] == 1:
				check[i + 1] = True
				for j in range(1, L):
					if arr[i + 1 + j] == arr[i + 1]:
						check[i + 1 + j] = True
					else: return False
			elif arr[i] - arr[i + 1] == -1:
				if check[i]:
					return False
				else:
					check[i] = True
					for j in range(1, L):
						if i - j < 0: return False
						if arr[i - j] == arr[i] and not check[i - j]:
							check[i - j] = True
						else: return False
			elif arr[i] == arr[i + 1]:
				continue
			else: return False
		except:
			return False

	return True

N, L = map(int, input().split())
Map, tmp = [], []
for _ in range(N):
	Map.append(list(map(int, input().split())))
for i in range(N):
	tmp.append([arr[i] for arr in Map])
Map += tmp
result = 0

for i in range(2 * N):
	if ramp(Map[i]):
		result += 1

print(result)