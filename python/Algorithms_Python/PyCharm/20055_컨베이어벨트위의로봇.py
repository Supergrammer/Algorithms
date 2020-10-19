import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dur = []
answer = 0

for i in list(map(int, input().split())):
    dur.append([i, False])

def move(dur):
    global cnt

    moved = [dur[-1]] + dur[:-1]
    if moved[N - 1][1] == True:
        moved[N - 1][1] = False

    for i in range(N - 2, -1, -1):
        if moved[i][1] == True:
            if moved[i + 1][0] != 0 and not moved[i + 1][1]:
                moved[i + 1][0] -= 1
                if moved[i + 1][0] == 0:
                    cnt += 1
                moved[i + 1][1] = True
                moved[i][1] = False

    if moved[N - 1][1] == True:
        moved[N - 1][1] = False

    if moved[0][0] != 0:
        moved[0][0] -= 1
        if moved[0][0] == 0:
            cnt += 1
        moved[0][1] = True

    return moved

def check():
    cnt = 0
    for block in dur:
        if block[0] == 0:
            cnt += 1
    return cnt

cnt = check()
while True:
    answer += 1
    dur = move(dur)
    if cnt >= K:
        break

print(answer)