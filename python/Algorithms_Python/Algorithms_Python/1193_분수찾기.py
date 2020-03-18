X = int(input())
n = 1
sum = 0

while(sum < X):
    sum += n
    n += 1

idx = sum - n + 2
c = X - idx
if n % 2 == 0:
    a, b = n - 1, 1
else:
    a, b = 1, n - 1
    c = -c

a -= c
b += c

print("{}/{}".format(a, b))