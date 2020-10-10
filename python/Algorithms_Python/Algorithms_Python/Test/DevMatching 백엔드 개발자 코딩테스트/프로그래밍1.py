import datetime
import re

def solution(n, customers):
	answer = 0
	kiosk = [[] for _ in range(n)]
	now = 0

	for customer in customers:
		tmp = list(map(int, re.split(' |/|:', customer)))
		start = datetime.datetime(2021, tmp[0], tmp[1], tmp[2], tmp[3], tmp[4])
		end = start + datetime.timedelta(minutes=tmp[5])
		now = start

		matched = False
		for i in range(n):
			if not kiosk[i]:
				kiosk[i].append([start, end])
				matched = True
				break
		
		if not matched:
			nxt = n
			mn = start + datetime.timedelta(days=100)
			for i in range(n):
				if mn >= kiosk[i][-1][1]:
					mn = kiosk[i][-1][1]
					nxt = i
			kiosk[i].append([start, end])

		for i in kiosk:
			answer = max(answer, len(i))
	return answer

print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))