import sys
input = sys.stdin.readline

dice = list(map(int, input().split()))
pieces = [0, 0, 0, 0]
Map = {}
answer = 0

def mapping():
    for i in range(20):
        Map[i * 2] = (i + 1) * 2

    for key, val in [['13', '16'], ['16', '19'], ['19', '25'],
                    ['22', '24'], ['24', '25'],
                    ['28', '27'], ['27', '26'], ['26', '25'],
                    ['25', '30'], ['30', '35'], ['35', 40],
                    [40, -1]]:
        Map[key] = val

def move(piece, cpypieces, die):
    now = cpypieces[piece]
    if now == 10: dst = '13'
    elif now == 20: dst = '22'
    elif now == 30: dst = '28'
    else: dst = Map[now]

    for i in range(die - 1):
        if dst == -1:
            break
        dst = Map[dst]

    if dst != -1:
        for i in range(4):
            if cpypieces[i] == dst:
                return False

    cpypieces[piece] = dst
    return True

def turn(pieces, order, score):
    if order == 10:
        global answer
        answer = max(answer, score)
        return

    for i in range(4):
        if pieces[i] == -1:
            continue

        cpypieces = pieces[:]
        if not move(i, cpypieces, dice[order]):
            continue

        turn(cpypieces, order + 1, score + (int(cpypieces[i])
             if cpypieces[i] != -1 else 0))
    return

mapping()
turn(pieces, 0, 0)

print(answer)