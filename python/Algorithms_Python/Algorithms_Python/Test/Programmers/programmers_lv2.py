import math

def solution1(nums):
    map = {}
    for i in nums:
        map[i] = True
        
    if len(map) > len(nums) / 2:
        return len(nums) / 2
    return len(map)

def solution2(brown, yellow):
    div = []
    area = brown + yellow
    area_sqr = math.ceil(math.sqrt(area))
    
    for i in range(2, area_sqr + 1):
        if area % i == 0:
            div.append([area // i, i])
            
    for arr in div:
        if (arr[0] - 2) * (arr[1] - 2) == yellow:
            return arr