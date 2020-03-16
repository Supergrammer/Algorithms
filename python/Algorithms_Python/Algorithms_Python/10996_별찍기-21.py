N = int(input())

for i in range(1, N + 1):
    print("* " * (int(N / 2) + N % 2))
    print(" *" * int(N / 2))