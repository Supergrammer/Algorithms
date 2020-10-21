# import sys
# input = sys.stdin.readline
#
# N, M, K = map(int, input().split())
# planets = []
# Map = [[[] for _ in range(N)] for _ in range(N)]
# dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
#
# for i in range(M):
#     y, x, m, s, d = map(int, input().split())
#     y -= 1; x -= 1
#     Map[y][x].append(i)
#     planets.append([y, x, m, s % N, d])
#
# def move():
#     cpyMap = [[[] for _ in range(N)] for _ in range(N)]
#     for i in range(len(planets)):
#         if planets[i]:
#             y, x, m, s, d = planets[i]
#             y = (y + dir[d][0] * s + N) % N
#             x = (x + dir[d][1] * s + N) % N
#             cpyMap[y][x].append(i)
#             planets[i] = [y, x, m, s, d]
#
#     return cpyMap
#
# def collide(arr):
#     Odd, Even = False, False
#     y, x = planets[arr[0]][:2]
#     m, s = 0, 0
#     divided = []
#
#     for i in arr:
#         pm, ps, pd = planets[i][2:]
#         m += pm; s += ps
#         if pd % 2 == 0: Even = True
#         else: Odd = True
#         planets[i] = []
#
#     m //= 5; s //= len(arr)
#     if m == 0:
#         return divided
#
#     if Odd and Even:
#         for i in [1, 3, 5, 7]:
#             divided.append([y, x, m, s, i])
#     else:
#         for i in [0, 2, 4, 6]:
#             divided.append([y, x, m, s, i])
#
#     return divided
#
# def totalmass():
#     answer = 0
#     for planet in planets:
#         if planet:
#             answer += planet[2]
#     return answer
#
# for _ in range(K):
#     Map = move()
#     for i in range(N):
#         for j in range(N):
#             if len(Map[i][j]) > 1:
#                 divided = collide(Map[i][j])
#                 Map[i][j] = []
#                 for k in divided:
#                     planets.append(k)
#                     Map[i][j].append(len(planets) - 1)
# print(totalmass())

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
Map = [[[] for _ in range(N)] for _ in range(N)]
planets = []
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
answer = 0

for i in range(M):
    y, x, m, s, d = map(int, input().split())
    Map[y - 1][x - 1].append(i)
    planets.append([y - 1, x - 1, m, s, d])

def collide(arr):
    y, x = planets[arr[0]][:2]
    tm, ts = 0, 0
    Odd, Even = False, False
    divided = []

    for planet in arr:
        m, s, d = planets[planet][2:]
        if d % 2 == 0: Even = True
        else: Odd = True
        tm += m; ts += s
        planets[planet] = []

    tm //= 5; ts //= len(arr)
    if tm == 0:
        return divided

    if Odd and Even:
        for i in [1, 3, 5, 7]:
            divided.append([y, x, tm, ts, i])
    else:
        for i in [0, 2, 4, 6]:
            divided.append([y, x, tm, ts, i])

    return divided

def move():
    cpyMap = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(planets)):
        if planets[i]:
            y, x, m, s, d = planets[i]
            y = (y + dir[d][0] * s + N) % N
            x = (x + dir[d][1] * s + N) % N
            planets[i] = [y, x, m, s, d]
            cpyMap[y][x].append(i)

    for i in range(N):
        for j in range(N):
            if len(cpyMap[i][j]) >= 2:
                divided = collide(cpyMap[i][j])
                cpyMap[i][j] = []
                for planet in divided:
                    planets.append(planet)
                    cpyMap[i][j].append(len(planets) - 1)

    return cpyMap

for _ in range(K):
    Map = move()
for planet in planets:
    if planet:
        answer += planet[2]

print(answer)