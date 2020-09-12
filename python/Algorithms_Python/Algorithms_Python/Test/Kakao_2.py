from itertools import combinations

def solution(orders, course):
    answer = []
    menu = set([])
    order = {}

    for i in range(len(orders)):
        menu = menu | set(orders[i])
        for j in orders[i]:
            try: order[j].append(i)
            except KeyError: order[j] = [i]

    menu = sorted(list(menu))
    delete = []
    for key in order:
        if len(order[key]) < 2:
            delete.append(key)

    for i in delete:
        del order[i]
        menu.remove(i)

    for i in course:
        combs = list(combinations(menu, i))
        tmp = []
        mx = 0

        for comb in combs:
            newMenu = set(range(len(order)))
            for j in comb:
                if len(newMenu) < 2: break
                newMenu = newMenu & set(order[j])

            if len(newMenu) >= 2:
                mx = max(mx, len(newMenu))
                tmp.append([len(newMenu), ''.join(comb)])

        for j in tmp:
            if j[0] == mx:
                answer.append(j[1])

    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))