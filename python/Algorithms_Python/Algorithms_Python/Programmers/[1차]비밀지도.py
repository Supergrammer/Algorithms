def solution(n, arr1, arr2):
    answer = []
    array = []
    
    for arr in [arr1, arr2]:
        for i in arr:
            tmp = []
            for j in range(n):
                tmp.append(i % 2)
                i //= 2
            array.append(list(reversed(tmp)))

    for i in range(n):
        answer.append('')
        for j in range(n):
            array[i][j] = array[i][j] | array[i + n][j]
            if array[i][j]:
                answer[i] += '#'
            else:
                answer[i] += ' '

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))