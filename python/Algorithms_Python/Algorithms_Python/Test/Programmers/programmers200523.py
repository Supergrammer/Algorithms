def check(p):
    chk = [0 for i in range(10)]
    p = str(p)
    
    for i in p:
        if chk[int(i)] == 0:
            chk[int(i)] = 1
        else:
            return False
    return True

def solution1(p):
    while True:
        p += 1
        if check(p):
            return p

def solution2(n):
    answer = 0
    
    while n != 0:
        p = 0
        while True:
            if pow(2, p) > n:
                break
            p += 1
    
        answer += pow(3, p - 1)
        n -= pow(2, p - 1)
    return answer

def solution3(total_sp, skills):
	vec = dict()
	N = 0

	for i in skills:
		for j in i:
			N = max(N, j)
		try:
			vec[i[0]].append(i[1])
		except KeyError:
			vec[i[0]] = [i[1]]

	answer = [0 for i in range(N)]

	for i in range(N):
		try:
			vec[i + 1]
		except KeyError:
			answer[i] = 1

	while True:
		for i in range(N):
			if answer[i] == 0:
				for j in vec[i + 1]:
					if answer[j - 1] != 0:
						answer[i] += answer[j - 1]
					else:
						answer[i] = 0
						break

		flag = True
		for i in range(N):
			if answer[i] == 0:
				flag = False
				break
		if flag: break

	sm = sum(answer)
	sp = total_sp / sm
	
	for i in range(N):
		answer[i] *= int(sp)
	return answer