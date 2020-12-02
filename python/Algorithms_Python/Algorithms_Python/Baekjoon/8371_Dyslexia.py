#import sys
#input = sys.stdin.readline

#N = int(input())
#str1 = list(map(ord, list(input().strip())))
#str2 = list(map(ord, list(input().strip())))

#answer = 0

#for i in range(N):
#	if str1[i] - str2[i]:
#		answer += 1

#print(answer)

import sys
input = sys.stdin.readline

N = int(input())
str1, str2 = input(), input()
answer = 0

for i in range(N):
	if str1[i] != str2[i]:
		answer += 1

print(answer)