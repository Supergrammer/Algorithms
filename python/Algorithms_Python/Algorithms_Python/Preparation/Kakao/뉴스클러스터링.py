def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    arr1, arr2 = [], []
    cntI, cntU = 0, 0

    for i in range(len(str1) - 1):
        isAlpha = True
        for j in str1[i:i+2]:
            if not 'a' <= j <= 'z':
                isAlpha = False
                break
        if isAlpha:
            arr1.append(str1[i:i+2])
    
    for i in range(len(str2) - 1):
        isAlpha = True
        for j in str2[i:i+2]:
            if not 'a' <= j <= 'z':
                isAlpha = False
                break
        if isAlpha:
            arr2.append(str2[i:i+2])

    cntU = len(arr1) + len(arr2)
    for i in arr1:
        if i in arr2:
            arr2.remove(i)
            cntI += 1
    cntU -= cntI

    if not cntU == 0:
        answer = int(cntI / cntU * 65536)
    else:
        answer = 65536
    return answer

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
print(solution(input(), input()))