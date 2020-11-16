def solution(n):
	memoi = [0] * (n + 1)
	memoi[1] = 1
	memoi[2] = 2

	for i in range(3, n + 1):
		memoi[i] = (memoi[i - 1] + memoi[i - 2]) % 1000000007

	return memoi[n]

print(solution(4))