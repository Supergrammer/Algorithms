def solution(n):
    answer = 0

    n = sorted(list(str(n)), reverse=True)
    answer = int(''.join(n))

    return answer

print(solution(118372))