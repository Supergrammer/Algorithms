import re

def solution(p, n):
	tmp = re.split(' |:', p)

	isAM = tmp[0]
	time = list(map(int, tmp[1:]))
	time[2] += n
	
	if isAM == 'PM' and time[0] != 12:
		time[0] += 12
	if isAM == 'AM' and time[0] == 12:
		time[0] -= 12

	if time[2] >= 60:
		time[1] += time[2] // 60
		time[2] = time[2] % 60
	if time[1] >= 60:
		time[0] += time[1] // 60
		time[1] = time[1] % 60
	if time[0] >= 24:
		time[0] = time[0] % 24

	time = list(map(str, time))
	for i in range(3):
		if len(time[i]) < 2:
			time[i] = '0' + time[i]

	answer = ':'.join(time)
	return answer

print(solution('PM 01:00:00', 10))
print(solution('PM 11:59:59', 1))