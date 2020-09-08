import re

def solution(s):
    answer = []
    dict = {}
    s = re.split('{|}|,', s)
    
    for c in s:
        if c != '':
            try:
                dict[int(c)] += 1
            except KeyError:
                dict[int(c)] = 1

    dict = sorted(dict.items(), reverse = True, key = lambda x : x[1])
    for a in dict:
        answer.append(a[0])

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))