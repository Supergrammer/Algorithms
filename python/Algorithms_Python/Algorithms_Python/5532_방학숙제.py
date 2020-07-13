import sys
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(L - max((A // C + (1 if A % C else 0)),\
	(B // D + (1 if B % D else 0))))