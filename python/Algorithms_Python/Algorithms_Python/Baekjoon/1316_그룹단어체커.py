N = int(input())
cnt = 0

for i in range(N):
    f = True
    S = input()
    alpha = [0 for i in range(26)]
    back = -1

    for j in range(len(S)):
        idx = ord(S[j]) - 97
        if back == idx: continue
        if alpha[idx] == 1:
            f = False
            break
        alpha[idx] = 1
        back = idx
    cnt += 1 if f else 0

print(cnt)