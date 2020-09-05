N = int(input())
ans = 0

def han(n):
    tmp = str(n)
    if len(tmp) == 1 or len(tmp) == 2: return True
    elif len(tmp) == 4: return False
    for i in range(len(tmp)):
        n1 = int(tmp[1]) - int(tmp[0])
        n2 = int(tmp[2]) - int(tmp[1])
        if n1 == n2: return True
        else: return False

for i in range(1, N + 1):
    ans += 1 if han(i) == True else 0

print(ans)