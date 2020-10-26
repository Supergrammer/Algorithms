import sys
input = sys.stdin.readline

while True:
	try:
		N, K = map(int, input().split())
	except:
		break
	seq = [0] + list(map(int, input().split()))
	seg = [sys.maxsize] * (2 ** 18)

	def seginit(start, end, node):
		if start == end:
			if seq[start] > 0: seg[node] = 1
			elif seq[start] < 0: seg[node] = -1
			else: seg[node] = 0
			return seg[node]

		mid = (start + end) // 2
		seg[node] = seginit(start, mid, node * 2) * seginit(mid + 1, end, node * 2 + 1)
		return seg[node]

	def segmul(start, end, node, left, right):
		if left > end or right < start: return 1
		if (left <= start and right >= end): return seg[node]

		mid = (start + end) // 2
		mul = segmul(start, mid, node * 2, left, right) * segmul(mid + 1, end, node * 2 + 1, left, right)
		return mul

	def segupdate(start, end, node, idx):
		if not start <= idx <= end:
			return seg[node]

		if start == end:
			if start == idx:
				if seq[start] > 0: seg[node] = 1
				elif seq[start] < 0: seg[node] = -1
				else: seg[node] = 0
			return seg[node]

		mid = (start + end) // 2
		seg[node] = segupdate(start, mid, node * 2, idx) * segupdate(mid + 1, end, node * 2 + 1, idx)
		return seg[node]

	seginit(1, N, 1)
	answer = ''

	for _ in range(K):
		c, i, j = input().split()
		i, j = int(i), int(j)
		
		if c == 'C':
			seq[i] = j
			segupdate(1, N, 1, i)
		else:
			mul = segmul(1, N, 1, i, j)
			if mul == 1: answer += '+'
			elif mul == -1: answer += '-'
			else: answer += '0'
	print(answer)