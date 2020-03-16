A, B = input().split()

A, B = list(A), list(B)
A.reverse()
B.reverse()

nA = int(''.join(A))
nB = int(''.join(B))

print(nA if nA > nB else nB)