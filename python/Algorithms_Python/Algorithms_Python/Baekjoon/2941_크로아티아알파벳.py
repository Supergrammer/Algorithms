S = input()
sum, idx = 0, 0
S += "  "

while(idx != len(S) - 2):
    if S[idx] != ' ':
        sum += 1
    if S[idx] == 'c':
        if S[idx + 1] in ['=', '-']: idx += 1
    elif S[idx] in ['l', 'n']:
        if S[idx + 1] == 'j': idx += 1
    elif S[idx] in ['s', 'z']:
        if S[idx + 1] == '=': idx += 1
    elif S[idx] == 'd':
        if S[idx + 1] == 'z' and S[idx + 2] == '=': idx += 2
        elif S[idx + 1] == '-': idx += 1
    idx += 1

print(sum)