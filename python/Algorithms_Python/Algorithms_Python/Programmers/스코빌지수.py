import heapq

def solution(scoville, K):
	answer = 0
	heapq.heapify(scoville)

	while scoville:
		scov = heapq.heappop(scoville)
		if scov >= K:
			break

		if not scoville:
			return -1
		nxtscov = heapq.heappop(scoville)
		scov = scov + nxtscov * 2
		answer += 1
		heapq.heappush(scoville, scov)

	return answer

print(solution([1, 2, 3, 9, 10, 12], 7))