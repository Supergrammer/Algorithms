A, B, C = map(int, input().split())

ben = C - B
if ben <= 0: print(-1)
else: print(int(A/ben) + 1)