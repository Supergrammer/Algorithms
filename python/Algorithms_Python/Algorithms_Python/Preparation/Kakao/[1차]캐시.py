from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    
    for c in cities:
        c = c.lower()
        isCacheHit = False

        if c in cache:
            answer += 1
            isCacheHit = True
        else:
            answer += 5

        if isCacheHit:
            cache.remove(c)
            cache.append(c)
        else:
            cache.append(c)
            if len(cache) > cacheSize:
                cache.popleft()

    return answer

print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
print(solution(2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))