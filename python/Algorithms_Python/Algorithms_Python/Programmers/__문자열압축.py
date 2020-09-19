def solution(s):
    answer, cnt = len(s), 0
    prv, nxt = '', ''
    for i in range(1, len(s) // 2 + 1):
        comp = len(s)
        prv = s[0:i]
        pointer = i

        while pointer <= len(s):
            nxt = s[pointer:pointer + i]

            if prv == nxt:
                comp -= i
                if cnt == 0:
                    comp += 1
                cnt += 1
            else: cnt = 0

            pointer += i
            prv = nxt

        answer = min(answer, comp)
    return answer

def solution2(s):
    answer = len(s)
    isRepeated = False
    prv, nxt = '', ''
    for i in range(1, len(s) // 2 + 1):
        comp = i
        prv = s[0:i]
        pointer = i

        while pointer <= len(s):
            nxt = s[pointer:pointer + i]
            if prv == nxt:
                if not isRepeated:
                    comp += 1
                    isRepeated = True
            else:
                comp += len(nxt)
                isRepeated = False

            pointer += i
            prv = nxt

        answer = min(answer, comp + len(s) % 2)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))