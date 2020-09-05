import sys

T = int(input())
while(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
    T -= 1