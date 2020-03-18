A, B, V = map(int, input().split())
cnt = 1

cnt += ((V - A) / (A - B)) + (1 if (V - A) % (A - B) != 0 else 0)
print(int(cnt))