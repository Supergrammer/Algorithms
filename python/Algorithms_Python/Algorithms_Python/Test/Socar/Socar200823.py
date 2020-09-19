import re

def solution1(bakery_schedule, current_time, K):
    pointer = 0
    schedule = []
    bread = 0
    ctime = list(map(int, re.split(':| ', current_time)))
    
    
    for sche in bakery_schedule:
        schedule.append(list(map(int, re.split(':| ', sche))))
    
    
    while True:
        if (schedule[pointer][0] < ctime[0]) or (schedule[pointer][0] == ctime[0] and schedule[pointer][1] < ctime[1]):
            pointer += 1
            if pointer >= len(schedule):
                return -1
            continue
        break
        
    while True:
        bread += schedule[pointer][2]
        if bread >= K:
            break
            
        pointer += 1
        if pointer >= len(schedule):
            return -1
    
    answer = (schedule[pointer][0] - ctime[0]) * 60 + schedule[pointer][1] - ctime[1]
    return answer


def check(x, n):
    if 0 <= x < n:
        return True
    else:
        return False

def solution2(drum):
    answer = 0
    N = len(drum[0])
    
    for i in range(N):
        y, x = 0, i
        counter = True
        flag = False
        
        while True:
            if drum[y][x] == '#':
                y += 1
            elif drum[y][x] == '>':
                x += 1
            elif drum[y][x] == '<':
                x -= 1
            elif drum[y][x] == '*':
                if counter:
                    counter = False
                    y += 1
                else:
                    break
                    
            if not check(x, N):
                break
                
            if y == N:
                flag = True
                break
        
        if flag:
            answer += 1
            
    return answer

mx = 0

def DFS(now, tip, time, delivery, visited, r):
    if time > 16:
        return

    global mx
    mx = max(mx, tip)
    
    for i in range(len(visited)):
        if visited[i] == 0:
            mt = abs(i // r - now // r) + abs(i % r - now % r)
            if time + mt <= delivery[i][0]:
                visited[i] = 1
                DFS(i, tip + delivery[i][1], time + mt, delivery, visited, r)
                visited[i] = 0

def solution3(r, delivery):
    visited = [1] + [0] * (r ** 2 - 1)
    DFS(0, delivery[0][1], 0, delivery, visited, r)
    
    answer = mx
    return mx