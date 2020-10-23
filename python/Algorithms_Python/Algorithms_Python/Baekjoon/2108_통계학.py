import sys
input = sys.stdin.readline

N = int(input())
arr, cnt = [], [0] * 8001
for _ in range(N):
	num = int(input())
	arr.append(num)
	cnt[num + 4000] += 1
arr.sort()

mx = max(cnt)
fnd = cnt.index(mx)
cnt[fnd] = 0
try:
	fnd = cnt.index(mx)
except ValueError:
	pass

print(round(sum(arr) / N))
print(arr[N // 2])
print(fnd - 4000)
print(arr[-1] - arr[0])