input()
li = list(map(int, input().split()))

mx = max(li)
for i in range(len(li)):
    li[i] = li[i] / mx * 100

print(sum(li) / len(li))