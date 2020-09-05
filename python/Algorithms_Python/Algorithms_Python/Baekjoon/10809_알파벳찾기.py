S = input()

for i in range(97, 123):
    try:
        print(S.index(chr(i)), end=' ')
    except ValueError:
        print(-1, end=' ')