N = int(input())

def fac(i):
    if i <= 1:
        return 1
    return fac(i - 1) * i

print(fac(N))