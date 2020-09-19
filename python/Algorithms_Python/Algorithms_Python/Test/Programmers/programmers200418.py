import itertools

def solution1(p, s):
    p, s, l = str(p), str(s), len(p)
    answer = 0
    for i in range(l):
        tmp = abs(int(p[i]) - int(s[i]))
        if tmp > 5:
            tmp = 10 - tmp
        answer += tmp
    return answer

def solution2(office, r, c, move):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    d = 0
    N = len(office)
    answer = office[r][c]
    office[r][c] = 0

    for i in move:
        if i == 'go':
            r_tmp, c_tmp = r + dy[d], c + dx[d]
            if (0 <= r_tmp < N and 0 <= c_tmp < N and office[r_tmp][c_tmp] != -1):
                r, c = r_tmp, c_tmp
                answer += office[r][c]
                office[r][c] = 0
        elif i == 'right':
            d = (d + 1) % 4
        elif i == 'left':
            d = (d - 1 + 4) % 4
    return answer

def solution3(numbers, K):
    answer = 9
    P = list(itertools.permutations(numbers, len(numbers)))
    for p in P:
        p = list(p)
        flag = True
        swap = 0
        
        prev = p[0]
        for i in p[1:]:
            next = i
            if abs(prev - next) > K:
                flag = False
                break
            prev = i
        if not(flag): continue
            
        for i in range(len(p)):
            if numbers[i] == p[i]: continue
            idx = p.index(numbers[i])
            p[i], p[idx] = p[idx], p[i]
            swap += 1
            
        answer = min(answer, swap)

    if answer == 9: return -1
    return answer