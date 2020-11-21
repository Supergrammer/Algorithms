# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
input = sys.stdin.readline

m = int(input())
Y, X = [], []

theta = [1.0, 1.0, 1.0]
lambd, delta = 0.1, 10 ** -4
threshold = 0.5

def h(xi:[]):
    matpro = sum([xi[i] * theta[i] for i in range(3)])
    return sigmoid(matpro)

def sigmoid(n):
    return 1 / (1 + math.exp(-n))

def cost():
    return sum([(-Y[i] * math.log(h(X[i])) - (1 - Y[i]) * math.log(1 - h(X[i]))) for i in range(m)]) / m\
        + lambd / (2 * m) * sum([theta[i] ** 2 for i in range(1, 3)])
    
def gradient():
    tmp = [0, 0, 0]
    for i in range(m):
        sm = (h(X[i]) - Y[i])
        for j in range(3):
            tmp[j] += X[i][j] * sm
    
    for i in range(3):
        tmp[i] /= m
        tmp[i] += lambd * theta[i] / m
        
    return tmp
    
for i in range(m):
    ipt = list(map(float, input().split()))
    Y.append(ipt[-1]); X.append([1] + ipt[:-1]);
    
prv = cost()
while True:
    grad = gradient()
    for i in range(3):
        theta[i] -= grad[i]
    
    nxt = cost()
    if nxt / prv > 1 - delta:
        break
    prv = nxt
    
n = int(input())
for i in range(n):
    x1, x2 = map(float, input().split())
    rst = h([1, x1, x2])
    if rst >= threshold:
        print(1)
    else: print(0)