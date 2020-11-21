# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
input = sys.stdin.readline

user_topk = int(input())
item_topk = int(input())
users = int(input()) + 1
items = int(input()) + 1
rows = int(input())

Rating = [[0] * items for _ in range(users)]
for _ in range(rows):
	ipt = list(map(float, input().split()))
	Rating[int(ipt[0])][int(ipt[1])] = ipt[2]
	
similarity = [[-1] * users for _ in range(users)]
for i in range(1, users):
	for j in range(1, users):
		if i == j:
			similarity[i][j] = 0
			continue
		
		if similarity[j][i] != -1:
			similarity[i][j] = similarity[j][i]
			continue
		
		matprd = 0
		for k in range(1, items):
			if Rating[i][k] != 0 and Rating[j][k] != 0:
				matprd += Rating[i][k] * Rating[j][k]
		
		Asq = math.sqrt(sum([Rating[i][k] ** 2 for k in range(1, items)]))
		Bsq = math.sqrt(sum([Rating[j][k] ** 2 for k in range(1, items)]))
		similarity[i][j] = matprd / (Asq * Bsq)
		
topk = [[] for _ in range(users)]
for i in range(1, users):
	visited = [False] * users
	for j in range(user_topk):
		idx, mx = 1, 0
		for k in range(1, users):
			if mx < similarity[i][k] and not visited[k]:
				idx, mx = k, similarity[i][k]
		topk[i].append(idx)
		visited[idx] = True
	
user = []
for i in range(int(input())):
	user.append(int(input()))

for i in user:
	recommend = [0] * items
	for j in range(1, items):
		up, down = 0, 0
		for k in topk[i]:
			if Rating[k][j] != 0:
				up += similarity[i][k] * Rating[k][j]
				down += similarity[i][k]
		if down == 0: continue
		recommend[j] = up / down
		
	visited = [False] * items
	for k in range(item_topk):
		idx, mx = 1, 0
		for l in range(1, items):
			if mx < recommend[l] and not visited[l]:
				idx, mx = l, recommend[l]
		print(idx, end=' ')
		visited[idx] = True
			
	print()