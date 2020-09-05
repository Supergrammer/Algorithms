cyc = input()
N = int(cyc)
tr = 0
while(1):
    if len(cyc) == 1: cyc = '0' + cyc
    sum = str(int(cyc[0]) + int(cyc[1]))
    cyc = cyc[1] + sum[len(sum) - 1]
    tr += 1
    if int(cyc) == N: break
print(tr)