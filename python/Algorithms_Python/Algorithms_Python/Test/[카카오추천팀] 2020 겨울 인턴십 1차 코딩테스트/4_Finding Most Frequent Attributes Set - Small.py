# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

ipt = sys.stdin.readlines()

attrib = int(ipt[0])
thresh = float(ipt[1])
numofrows = int(ipt[2])

dict = {}
answer = {}

for i in range(3, 3 + numofrows):
    arr = re.split(',', ipt[i].strip())
    for att in arr:
        tmp = att.split(sep='=')
        
        if not dict.get(tmp[0]):
            dict[tmp[0]] = {}
            
        if dict[tmp[0]].get(tmp[1]):
            dict[tmp[0]][tmp[1]].append(i - 3)
        else: dict[tmp[0]][tmp[1]] = [i - 3]
        
for key in dict.keys():
    for k, v in dict[key].items():
        if len(dict[key][k]) >= numofrows * thresh:
            if not answer.get(key):
                answer[key] = []
            answer[key].append((k, v))

key = list(answer.keys())
def printanswer(depth=0, index=0, arr=[], st=set()):
    if depth == attrib:
        print(','.join(arr))
        
    for i in range(index, len(key)):
        for j in answer[key[i]]:
            arr.append('='.join([key[i], j[0]]))
            nxt = set()
            
            if not st:
                nxt = set(j[1])
            else:
                nxt = st & set(j[1])
                
            if not len(nxt) < numofrows * thresh:
                printanswer(depth + 1, i + 1, arr, nxt)
            arr.pop()
        
printanswer()