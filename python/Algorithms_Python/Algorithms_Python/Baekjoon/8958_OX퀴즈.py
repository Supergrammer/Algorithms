T = int(input())
while(T):
    rst = input()
    com, scr = 0, 0
    for i in range(len(rst)):
        if rst[i] == 'O':
            com += 1
            scr += com
        else:
            com = 0
    print(scr)
    T -= 1