from collections import deque

def solution(progresses, speeds):
	answer = []
	
	progress = deque(progresses)
	speed = deque(speeds)

	while True:
		if not progress:
			break

		for i in range(len(progress)):
			if progress[i] >= 100: continue
			progress[i] += speed[i]

		distrib = 0
		while True:
			if progress and progress[0] >= 100:
				progress.popleft()
				speed.popleft()
				distrib += 1
			else: break

		if distrib:
			answer.append(distrib)

	return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))