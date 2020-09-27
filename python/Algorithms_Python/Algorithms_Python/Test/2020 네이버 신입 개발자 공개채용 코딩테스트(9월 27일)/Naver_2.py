def check(pyramid, length):
	for i in range(length - 1, 0, -1):
		for j in range(i):
			if pyramid[i][j] == None:
				return False
	return True

def solution(blocks):
	answer = []
	pyramid = []

	for i in range(len(blocks)):
		pyramid.append([None] * (i + 1))

	for i in range(len(blocks)):
		pyramid[i][blocks[i][0]] = blocks[i][1]

	while True:
		for i in range(len(pyramid) - 1):
			for j in range(len(pyramid[i])):
				tmp = [pyramid[i][j], pyramid[i + 1][j], pyramid[i + 1][j + 1]]
				cnt = 0
				for k in tmp:
					if k == None: cnt += 1
				if cnt != 1:
					continue

				if tmp[0] == None: tmp[0] = tmp[1] + tmp[2]
				elif tmp[1] == None: tmp[1] = tmp[0] - tmp[2]
				elif tmp[2] == None: tmp[2] = tmp[0] - tmp[1]

				pyramid[i][j], pyramid[i + 1][j], pyramid[i + 1][j + 1] = tmp

		if check(pyramid, len(pyramid)):
			break

	for pyra in pyramid:
		answer.extend(pyra)
	
	return answer

print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))