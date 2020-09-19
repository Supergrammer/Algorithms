def solution(dartResult):
    answer = 0
    num = ''
    score = []

    for c in dartResult:
        if '0' <= c <= '9':
            num += c
            continue

        elif c in ['S', 'D', 'T']:
            score.append(int(num))
            if c == 'D':
                score[-1] **= 2
            elif c == 'T':
                score[-1] **= 3
            num = ''

        elif c in ['*', '#']:
            if c == '*':
                try:
                    score[-1] *= 2
                    score[-2] *= 2
                except IndexError:
                    pass
            elif c == '#':
                score[-1] *= -1

    answer = sum(score)
    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))