import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
Map = {}
shortest = [sys.maxsize] * (V + 1)
shortest[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    if Map.get(u):
        Map[u].append([v, w])
    else:
        Map[u] = [[v, w]]

Q = [[0, K]]
while Q:
    d, p = heapq.heappop(Q)

    if Map.get(p) and shortest[p] >= d:
        for edge in Map[p]:
            nxt, nd = edge
            if d + nd < shortest[nxt]:
                shortest[nxt] = d + nd
                heapq.heappush(Q, (d + nd, nxt))

for i in shortest[1:]:
    if i == sys.maxsize:
        print('INF')
    else:
        print(i)