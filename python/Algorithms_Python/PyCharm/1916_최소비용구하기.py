import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
Map = [{} for _ in range(N + 1)]
shortest = [sys.maxsize] * (N + 1)

for _ in range(M):
    fr, to, d = map(int, input().split())
    if to in Map[fr]:
        Map[fr][to] = min(Map[fr][to], d)
    else:
        Map[fr][to] = d

fr, to = map(int, input().split())
shortest[fr] = 0

Q = [[0, fr]]
while Q:
    d, v = heapq.heappop(Q)
    if v == to: break
    for nv, nd in Map[v].items():
        if d + nd <= shortest[nv]:
            shortest[nv] = d + nd
            heapq.heappush(Q, (d + nd, nv))

print(shortest[to])