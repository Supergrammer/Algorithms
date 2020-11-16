from collections import deque

def solution1(bridge_length, weight, truck_weights):
	answer = 0
	totalw, index, done = 0, 0, 0

	for i in range(len(truck_weights)):
		truck_weights[i] = [truck_weights[i], -1]

	while True:
		answer += 1

		for i in range(len(truck_weights)):
			if truck_weights[i][1] != -1:
				truck_weights[i][1] += 1
				if truck_weights[i][1] > bridge_length:
					truck_weights[i][1] = -1
					totalw -= truck_weights[i][0]
					done += 1

		if index != len(truck_weights) and totalw + truck_weights[index][0] <= weight:
			truck_weights[index][1] = 1
			totalw += truck_weights[index][0]
			index += 1

		if done == len(truck_weights):
			return answer

def solution(bridge_length, weight, truck_weights):
	answer = 0
	tweight = 0

	truck = deque(truck_weights)
	Q = deque([])

	while True:
		answer += 1

		if Q:
			for i in range(len(Q)):
				Q[i][1] += 1
			if Q[0][1] > bridge_length:
				tweight -= Q[0][0]
				Q.popleft()

		if truck and truck[0] + tweight <= weight:
			Q.append([truck.popleft(), 1])
			tweight += Q[-1][0]

		if not truck and not Q:
			return answer


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))