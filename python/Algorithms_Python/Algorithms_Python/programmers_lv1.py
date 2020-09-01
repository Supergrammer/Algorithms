def solution1(arr):
    answer = arr
    answer.pop(answer.index(min(answer)))

    if answer:
        return answer
    return [-1]

def solution2(n):
    answer = list(str(n))
    answer.sort(reverse=True)

    return int(''.join(answer))