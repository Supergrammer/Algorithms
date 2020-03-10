A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)
dic = [0 for i in range(10)]

for i in range(len(mul)):
    dic[int(mul[i])] += 1
for i in range(10):
    print(dic[i])