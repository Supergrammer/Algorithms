n = int(input())

def Fibonacci(i):
    if i == 0: return 0
    if i == 1 or i == 2: return 1

    return Fibonacci(i - 1) + Fibonacci(i - 2)

print(Fibonacci(n))