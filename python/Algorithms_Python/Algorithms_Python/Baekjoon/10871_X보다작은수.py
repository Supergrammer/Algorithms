N, X = map(int, input().split())
li = list(map(int, input().split()))
for i in range(N):
    if (li[i] < X): print(li[i], end=" ")