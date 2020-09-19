def isRight(s):
    cnt = 0

    for c in s:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def solution(p):
    cnt = 0
    u, v = '', ''

    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u, v = p[:i + 1], p[i + 1:]
            break

    if v != '':
        v = solution(v)

    if not isRight(u):
        rev = ''
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                rev += ')'
            else:
                rev += '('
        u = '(' + v + ')' + rev
    else:
        u = u + v

    return u

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))