C = int(input())
while(C):
    li = list(map(int, input().split()))[1:]
    avg = sum(li) / len(li)
    cnt = 0

    for i in range(len(li)):
        if li[i] > avg:
            cnt += 1
    print("%.3f" %(cnt / len(li) * 100) + "%")
    C -= 1