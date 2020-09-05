num = [0 for i in range(10001)]

def d(n):
    sum = n
    tmp = str(n)
    for i in range(len(tmp)):
        sum += int(tmp[i])
    if sum <= 10000:
        num[sum] = 1
        d(sum)

for i in range(1, len(num)):
    if num[i] == 0:
        print(i)
        d(i)